import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# Input 1-D arrays 
#array1: can be both LS or GW
#array2: can be both LS or GW

# Computing DTW distance
distance, path = fastdtw(array1, array2, dist=euclidean)

print("DTW distance:", distance)
print("DTW path:", path)
