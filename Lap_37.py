"""
Day 37 Activity: Dot Product
Tasks:
1) Compute dot product of two vectors
2) Compute cosine similarity
3) Interpret results
"""

import numpy as np

# Provided vectors (edit if you want different values)
a = np.array([1.0, 2.0, 3.0])
b = np.array([0.5, 1.0, 1.5])

#Task 1: Compute dot product of two vectors
dot_product = np.dot(a, b)

#Task 2: Compute cosine similarity
cosine_similarity = dot_product / (np.linalg.norm(a) * np.linalg.norm(b))

#Task 3: Interpret results
print("Vector a:", a)
print("Vector b:", b)
print("Dot product:", dot_product)
print("Cosine similarity:", cosine_similarity)
print("The cosine similarity is close to 1, indicating that the vectors are highly similar and point in the same direction.")


# TODO: Compute dot and cosine similarity
