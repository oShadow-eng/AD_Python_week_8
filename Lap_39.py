"""
Day 39 Activity: Broadcasting
Tasks:
1) Normalize matrix by row using broadcasting
2) Verify each row has unit norm
"""

import numpy as np

# Provided matrix (edit if you want different values)
X = np.array([
    [3.0, 4.0],
    [1.0, 2.0],
    [0.0, 5.0],
])

#Task 1: Normalize each row of X using broadcasting
row_norms = np.linalg.norm(X, axis=1, keepdims=True)
X_normalized = X / row_norms

#Task 2: Verify each row has unit norm
print("Normalized matrix X:")
print(X_normalized)

print("Norms of each row:")
print(np.linalg.norm(X_normalized, axis=1))



# TODO: Compute row_norms and X_normalized
# TODO: Print norms
