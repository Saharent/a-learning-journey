import numpy as np

cat = np.array([0.8, 0.7])
dog = np.array([0.75, 0.72])
airplane = np.array([0.1, -0.9])

distance = np.linalg.norm(cat - airplane)

print(distance)