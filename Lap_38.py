"""
Day 38 Activity: Matrices
Tasks:
1) Create data matrix X and weight matrix W
2) Compute X @ W
3) Inspect shapes and transpose
"""

import numpy as np

#Task 1: Create data matrix X and weight matrix W
X = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])
W = np.array([
    [0.1, -0.2],
    [0.4, 0.0],
    [-0.3, 0.5],
])

#Task 2: Compute X @ W
Y = X @ W

#Task 3: Inspect shapes and transpose
print("Shape of X:", X.shape)
print("Shape of W:", W.shape)
print("Shape of Y:", Y.shape)
print("Transpose of X:", X.T)

# TODO: Compute Y = X @ W
# TODO: Print shapes
