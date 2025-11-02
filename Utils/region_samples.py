from get_cords import get_cords

def find_first_greater(cand, vals):
    for val in vals:
        start, end = val
        if cand >= start and cand <= end:
            return vals.index(val)

def categorize_ordinary_samples(coors, x_regions, y_regions, y_lim=220):
    region_dict = {}
    for i in range(20):
        region_dict[i] = []
    for cor in coors:
        if cor[1] <= y_lim:
            x, y, z = cor
            x_idx = find_first_greater(x, x_regions)
            y_idx = find_first_greater(y, y_regions) + 1
            region = x_idx + len(x_regions) * (y_idx - 1)
            region_dict[region].append(cor)
    return region_dict

def categorize_conditioned_samples(coors, region_dict, start_cnt=12, start_cor=(0, 240, 0)):
    info_dict = {
        12: [(0,70), (235,305)],
        13: [(70,  145), (235, 330)],
        14: [(145, 210), (235, 330)],
        15: [(210, 282), (235, 305)],
        16: [(0, 70), (305, 400)],
        17: [(70, 145), (330, 400)],
        18: [(145, 210), (330, 400)],
        19: [(210, 282), (305, 400)],
    }
    start_idx = coors.index(start_cor)
    for i in range(start_idx, len(coors)):
        x, y, z = coors[i]
        for key, [x_region, y_region] in info_dict.items():
            strat_x, end_x = x_region
            strat_y, end_y = y_region
            if x >= strat_x and x <= end_x and y >= strat_y and y <= end_y:
                region_dict[key].append(coors[i])
    return region_dict

tot_coords = get_cords()
coordinates = [list(cor.values())[0] for cor in tot_coords]
x_regions = [(0, 75), (75, 155), (155, 235), (235, 282)]
y_regions = [(0, 75), (75, 155), (155, 235)]
regions_dict = categorize_ordinary_samples(coordinates, x_regions, y_regions)
regions_dict = categorize_conditioned_samples(coordinates, regions_dict)
print(*zip(regions_dict.keys(), [len(val) for val in regions_dict.values()]), sep='\n')
print(*regions_dict.items(), sep='\n\n')

sum = 0
for val in regions_dict.values():
    sum += len(val)
print('Total Number of Categorized Samples:', sum)
import matplotlib.pyplot as plt

def visualize_test_points(test_coors):
    # Extract x, y coordinates from test_coors
    x_vals = [coor[0] for coor in test_coors]
    y_vals = [coor[1] for coor in test_coors]

    # Create a 2D scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x_vals, y_vals, c='blue', marker='o', label='Test Points')

    # Labeling the plot
    plt.title('2D Test Points Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.show()

# Example usage:
visualize_test_points(test_coors)