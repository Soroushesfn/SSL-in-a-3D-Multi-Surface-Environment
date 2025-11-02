# Envalueing the 2D grids cell
for x in np.arange(x_min, x_max, grid_resolution):
    for y in np.arange(y_min, y_max, grid_resolution):
            # Initialize a variable to accumulate likelihood for the current grid point
            likelihood = 0

            # Calculate distances from the grid point to each microphone
            d1 = np.sqrt((x - p1[0])**2 + (y - p1[1])**2 + (z - p1[2])**2)
            d2 = np.sqrt((x - p2[0])**2 + (y - p2[1])**2 + (z - p2[2])**2)
            d3 = np.sqrt((x - p3[0])**2 + (y - p3[1])**2 + (z - p3[2])**2)

            # Calculate expected TDOA based on these distances
            expected_tau_12 = (d1 - d2) / c
            expected_tau_13 = (d1 - d3) / c
            expected_tau_23 = (d2 - d3) / c

            # Compare the expected TDOAs with the measured TDOAs
            # Update the likelihood of the sound source being at the current grid point
            likelihood += np.exp(-((tau_12 - expected_tau_12)**2) / (2 * sigma**2))
            likelihood += np.exp(-((tau_13 - expected_tau_13)**2) / (2 * sigma**2))
            likelihood += np.exp(-((tau_23 - expected_tau_23)**2) / (2 * sigma**2))

            # Store the likelihood in the heatmap array
            heatmap[x_idx, y_idx] = likelihood

# Normalizing the heatmap values
heatmap = heatmap / np.max(heatmap)

# 3D plotting the heatmap
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='2d')
x, y, z = np.indices(heatmap.shape)
ax.voxels(x, y, heatmap > threshold, facecolors='red', edgecolor='k')
plt.show()
