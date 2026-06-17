import numpy as np 
import math

def euclidean_distance(v1, v2):
    distance= np.linalg.norm(v2 - v1)

    return distance


dist = euclidean_distance( np.array([1,2]),
    np.array([4,6]))

print(dist)

