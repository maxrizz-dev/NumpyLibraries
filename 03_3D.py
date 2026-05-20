import numpy as np

# Create a 3D array

arr3d = np.array([[ [1,2,3],
                    [4,5,6],
                    [7,8,9]]]) 

print("3D Array:")
print(arr3d)

# Check attributes of the 3D array
print("\nShape of the 3D array:", arr3d.shape)  # Output: (1, 3, 3)
print("Data type of the 3D array:", arr3d.dtype) 
print("Number of dimensions:", arr3d.ndim)  # Output: 3
print("Size of the 3D array:", arr3d.size)  # Output: 9