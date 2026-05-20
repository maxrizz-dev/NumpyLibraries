#create array with default values

import numpy as np

# Create an array of zeros
zeros_array = np.zeros((2, 3))  # 2 rows and 3 columns
print("Array of zeros:")
print(zeros_array)

# Create an array of ones
ones_array = np.ones((3, 4))  # 3 rows and 4 columns
print("\nArray of ones:")
print(ones_array)

# Create an array filled with a specific value
full_array = np.full((2, 2), 7)  # 2 rows and 2 columns filled with 7
print("\nArray filled with 7:")
print(full_array)


# Create an array with a range of values (start, stop, step)
range_array = np.arange(0, 10, 2) 
print("\nArray with a range of values:")
print(range_array)


# Create an identity matrix
identity_matrix = np.eye(4)  # Identity matrix of size 4x4
print("\nIdentity Matrix of size 4x4:")
print(identity_matrix)


# Create an array with linearly spaced values (start, stop, number of points)
linspace_array = np.linspace(0, 1, 5)
print("\nArray with linearly spaced values:")
print(linspace_array) # Output: [0.  0.25 0.5  0.75 1.]


# Create an array of random numbers between 0 and 1 (floats)
random_array = np.random.rand(3, 3)  # 3x3 array
print("\nArray of random numbers between 0 and 1:")
print(random_array)

# Create an array of random integers between 0 and 10
random_int_array = np.random.randint(0, 10, (2, 5)) #(start, stop, shape)
print("\nArray of random integers between 0 and 10:")
print(random_int_array)

# Create an array and reshape it
reshaped_array = np.arange(12).reshape((3, 4))
print("\nReshaped Array (3x4):")
print(reshaped_array)

# Create a 2D array and flatten it to 1D
flattened_array = np.array([[1, 2, 3],
                            [4, 5, 6]]).flatten()
print("\nFlattened Array:")
print(flattened_array)

