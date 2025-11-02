import math

def tdoas(x, y):
    mic_pos = [(76.6, 0), (61.7, 0), (57.7, 0), (54, 0)]
    
    distances = []
    for i in range(0, 4): 
        distances.append(math.sqrt((x - mic_pos[i][0])**2 + (y - mic_pos[i][1])**2))
    
    toas = []
    for i in range(0, 4):
        toas.append(distances[i] / 343)
    
    tdoas = {
        'tdoa01': toas[0] - toas[1],
        'tdoa02': toas[0] - toas[2],
        'tdoa03': toas[0] - toas[3],
        'tdoa12': toas[1] - toas[2],
        'tdoa13': toas[1] - toas[3],
        'tdoa23': toas[2] - toas[3]
    }
    
    return tdoas