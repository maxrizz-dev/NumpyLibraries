import numpy as np

#create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)  # Output: [1 2 3 4 5]


#check attributes of the array
print("Shape of the array:", arr1d.shape)  # Output: (5,)
print("Data type of the array:", arr1d.dtype)  # Output: int64 (or int32 depending on the system)
print("Number of dimensions:", arr1d.ndim)  # Output: 1
print("Size of the array:", arr1d.size)  # Output: 5

#accessing elements
print(arr1d[0])  # Output: 1
print(arr1d[2])  # Output: 3
print(arr1d[-1])  # Output: 5
#slicing  (start:stop:step)
print(arr1d[1:4])  # Output: [2 3 4]
print(arr1d[:3])  # Output: [1 2 3]
print(arr1d[3:5])  # Output: [4 5]