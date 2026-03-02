"""
Day 36 Activity: Vectors
Tasks:
1) Create feature and weight vectors
2) Compute vector addition and scalar multiplication
3) Compute norms and inspect shapes
"""

import numpy as np

#Task 1: Create feature and weight vectors
feature = np.array([30.0, 50.0, 10.0])
weights = np.array([0.05, 0.8, -0.1])

#Task 2: Compute vector addition and scalar multiplication
# Vector addition
vector_addition = feature + weights
# Scalar multiplication
scalar_multiplication = 2 * feature

#Task 3: Compute norms and inspect shapes
# Norms
norm_feature = np.linalg.norm(feature)
norm_weights = np.linalg.norm(weights)
norm_vector_addition = np.linalg.norm(vector_addition)
norm_scalar_multiplication = np.linalg.norm(scalar_multiplication)

print("Norm of feature:", norm_feature)
print("Norm of weights:", norm_weights)
print("Norm of vector addition:", norm_vector_addition)
print("Norm of scalar multiplication:", norm_scalar_multiplication)
print("feature shape:", feature.shape)
print("weights shape:", weights.shape)
