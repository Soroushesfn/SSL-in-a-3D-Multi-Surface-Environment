from get_cords import get_cords
import shutil
import os
from natsort import natsorted

tot_coords = get_cords()
folder_names = ['nima, behrad, me']
y_vals = [x * 20 for x in range(21)]
coordinates = [list(cor.values())[0] for cor in tot_coords]
indexes = [i for i in range(315)]

import os
import shutil

# Define the paths to the three directories
me_folder = "samples/me"
behrad_folder = "samples/behrad"
nima_folder = "samples/nima"

# Define the destination folders for nima, me, behrad
dest_nima = "E:/final_samples/k1"
dest_me = "E:/final_samples/k2"
dest_behrad = "E:/final_samples/k3"

# Ensure destination directories exist
os.makedirs(dest_nima, exist_ok=True)
os.makedirs(dest_me, exist_ok=True)
os.makedirs(dest_behrad, exist_ok=True)

def sorted_directory_listing_with_os_listdir(directory):
    items = os.listdir(directory)
    sorted_items = natsorted(items)
    return sorted_items

# Iterate through each folder in 'me'
idx = 0
for me_y_folder in sorted_directory_listing_with_os_listdir(me_folder):
    print(f'\n\n************************\nAt y={me_y_folder}************************')
    me_y_folder_path = os.path.join(me_folder, me_y_folder)
    
    if os.path.isdir(me_y_folder_path):
        # Get the corresponding folders in 'nima' and 'behrad'
        nima_y_folder_path = os.path.join(nima_folder, me_y_folder)
        behrad_y_folder_path = os.path.join(behrad_folder, me_y_folder)
        
        if not os.path.isdir(nima_y_folder_path) or not os.path.isdir(behrad_y_folder_path):
            print(f"Corresponding folder not found for {me_y_folder}")
            continue
        
        # Iterate through each wav file in the 'me' folder
        for me_file in sorted_directory_listing_with_os_listdir(me_y_folder_path):
            if me_file.endswith(".wav"):
                me_file_path = os.path.join(me_y_folder_path, me_file)
                me_file_client = me_file.replace('server_', '')
                # Find the corresponding file in 'nima' and 'behrad'
                nima_file_path = os.path.join(nima_y_folder_path, me_file_client)
                behrad_file_path = os.path.join(behrad_y_folder_path, me_file_client)
                
                if os.path.exists(nima_file_path) and os.path.exists(behrad_file_path):
                    # Find the corresponding coordinates (assuming index is based on folder naming)
                    y_value = int(me_y_folder)
                    coord = coordinates[idx]
                    idx += 1
                    
                    if coord:
                        # Create new filenames with the coordinates and suffix 1, 2, 3 for nima, me, behrad
                        base_filename = f"{coord}_"
                        
                        new_nima_filename = base_filename + "1.wav"
                        new_me_filename = base_filename + "2.wav"
                        new_behrad_filename = base_filename + "3.wav"
                        print(me_file_path)
                        print(new_me_filename)
                        # Copy and rename the files to the destination folders
                        # shutil.copy2(nima_file_path, os.path.join(dest_nima, new_nima_filename))
                        # shutil.copy2(me_file_path, os.path.join(dest_me, new_me_filename))
                        # shutil.copy2(behrad_file_path, os.path.join(dest_behrad, new_behrad_filename))
                        
                        print(f"Processed: {me_file} for y={y_value} with coordinate={coord}")
                else:
                    print(f"Corresponding file not found for {me_file} in nima or behrad")
