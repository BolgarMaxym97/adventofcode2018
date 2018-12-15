import numpy as np
from scipy.spatial import distance

points = np.loadtxt('../../dist/6.txt', delimiter=', ')

# build a grid of the appropriate size - note the -1 and +2 to ensure all points
# are within the grid
xmin, ymin = points.min(axis=0) - 1
xmax, ymax = points.max(axis=0) + 2

# and use mesgrid to build the target coordinates
xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

# happily scipy.spatial.distance has cityblock (or manhatten) distance out
# of the box
cityblock = distance.cdist(points, targets, metric='cityblock')

# turns out using this method the solution is easier that before - simply
# sum the distances for each possible grid location
origin_distances = cityblock.sum(axis=0)
# set the value of appropriate distances to 1, with the remainder as zero
region = np.where(origin_distances < 10000, 1, 0)
# and the sum is the result.
print(region.sum())

# again, a nice picture for good measure
import matplotlib.pyplot as plt
plt.imshow(region.reshape(xgrid.shape))
plt.colorbar()
plt.show()