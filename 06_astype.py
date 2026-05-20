#convert data types
import numpy as np
# Create a 1D array of integers
arr_int = np.array([1, 2, 3, 4, 5])
print("Original array (integers):")
print(arr_int)
print(arr_int.dtype)  # Output: int64 (or int32 depending on the system)
# Convert the array to float
arr_float = arr_int.astype(float)
print("\nArray converted to float:")
print(arr_float)