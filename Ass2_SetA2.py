import numpy as np
from numpy.linalg import norm
p1 = [1, 2, 3]
p2 = [4, 5, 6]
dist = norm(np.array(p1) - np.array(p2))
print("Euclidean distance between the two data points:", dist)