import socket
import threading
import os
import pyaudio
import wave
import keyboard

# Global event to control recording start and stop
recording_event = threading.Event()
stop_event = threading.Event()

# Function to handle recording audio
def record_audio(filename):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 4
    fs = 16000  # Record at 44100 samples per second
    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []

    while not stop_event.is_set():
        if recording_event.is_set():
            data = stream.read(chunk)
            frames.append(data)
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def server_program():
    host = "0.0.0.0"  # Listen on all interfaces
    port = 5000  # Port number

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(3)  # Listen for up to 3 connections

    clients = []
    print("Server is running. Waiting for connections...")

    def handle_input():
        counter = 1
        while True:
            if keyboard.is_pressed('s'):
                # Start recording on the server and notify clients
                recording_event.set()
                stop_event.clear()
                filename = os.path.join("samples", f"server_recording_{counter}.wav")
                threading.Thread(target=record_audio, args=(filename,)).start()
                for client in clients:
                    client.send('s'.encode())
                counter += 1
                print("Recording started...")
                while keyboard.is_pressed('s'):
                    continue
            elif keyboard.is_pressed('q'):
                # Stop recording on the server and notify clients
                recording_event.clear()
                stop_event.set()
                for client in clients:
                    client.send('q'.encode())
                print("Recording stopped.")
                while keyboard.is_pressed('q'):
                    continue
            elif keyboard.is_pressed('x'):
                # Exit command to all clients
                for client in clients:
                    client.send('x'.encode())
                print("Exit command sent. Closing server.")
                for client in clients:
                    client.close()
                server_socket.close()
                os._exit(0)  # Force exit the program
                break

    threading.Thread(target=handle_input).start()

    while True:
        conn, address = server_socket.accept()  # Accept new connection
        clients.append(conn)
        print(f"Connected to: {address}")

if __name__ == "__main__":
    if not os.path.exists("samples"):
        os.makedirs("samples")
    server_program()
