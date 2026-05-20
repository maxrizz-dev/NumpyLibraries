import numpy as np

# Create a 2D array
arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6]])
print("2D Array:")
print(arr2d)

# Check attributes of the 2D array
print("\nShape of the 2D array:", arr2d.shape)  # Output: (2, 3)
print("Data type of the 2D array:", arr2d.dtype)  # Output: int64 (or int32 depending on the system)
print("Number of dimensions:", arr2d.ndim)  # Output: 2
print("Size of the 2D array:", arr2d.size)  # Output: 6

# Accessing elements in a 2D array (row, column)
print(arr2d[0, 0])  # Output: 1 (first row, first column)
print(arr2d[1, 2])  # Output: 6 (second row, third column)

# Slicing a 2D array (row, column)
print(arr2d[0, :])  # Output: [1 2 3] (first row)