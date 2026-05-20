#create arrays and perform aggregate functions

import numpy as np
# Create a 2D array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("Original 2D Array:")
print(arr2d)

# Perform aggregate functions
print("\nSum of all elements:", np.sum(arr2d))  # Output: 45
print("Product of all elements:", np.prod(arr2d))  # Output: 362880
print("Mean of all elements:", np.mean(arr2d))  # Output: 5.0
print("Minimum element:", np.min(arr2d))  # Output: 1
print("Maximum element:", np.max(arr2d))  # Output: 9
print("Standard deviation:", np.std(arr2d))  # Output: 2.582089957298186
print("Variance:", np.var(arr2d))  # Output: 6.666666666666667