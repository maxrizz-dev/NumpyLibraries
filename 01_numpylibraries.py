import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")


# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2d)

# Create a 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(arr3d)

# attributes of arrays
print("\nShape of 1D array:", arr1d.shape)
print("Shape of 2D array:", arr2d.shape)
print("Shape of 3D array:", arr3d.shape)
print("\nData type of 1D array:", arr1d.dtype)
print("Data type of 2D array:", arr2d.dtype)   
print("Data type of 3D array:", arr3d.dtype)
print("\nNumber of dimensions in 1D array:", arr1d.ndim)
print("Number of dimensions in 2D array:", arr2d.ndim)
print("Number of dimensions in 3D array:", arr3d.ndim)
print("\nSize of 1D array:", arr1d.size)
print("Size of 2D array:", arr2d.size)
print("Size of 3D array:", arr3d.size)


#arry initialization methods
# Create an array of zeros
zeros_array = np.zeros((2, 3))
print("\nArray of zeros:")
print(zeros_array)
# Create an array of ones
ones_array = np.ones((3, 4))
print("\nArray of ones:")
print(ones_array)
# Create an array of a specific value
full_array = np.full((2, 2), 7)
print("\nArray filled with 7:")
print(full_array)
# Create an array with a range of values # (start, stop, step) 
range_array = np.arange(0, 10, 2)
print("\nArray with a range of values (0 to 10 with step 2):")
print(range_array)
# Create an array with linearly spaced values # (start, stop, number of points)
linspace_array = np.linspace(0, 1, 5)
print("\nArray with linearly spaced values (0 to 1 with 5 points):")
print(linspace_array)

#identity matrix
identity_matrix = np.eye(4)
print("\nIdentity Matrix of size 4x4:")
print(identity_matrix)

#random number generation
# Create an array of random integers between 100 and 1000 with shape (3, 3)
random_int_array = np.random.randint(100, 1000, (3, 3))
print("\nArray of random integers between 100 and 1000:")
print(random_int_array)


#indexing and slicing on arrays
# Create a 2D array for indexing and slicing
index_array = np.array([[10, 20, 30], 
                        [40, 50, 60],
                        [70, 80, 90]])
print("\nOriginal Array:")
print(index_array)
# Indexing: Accessing a specific element
element = index_array[1, 2]  # Accessing the element at row 1, column 2
print("\nElement at row 1, column 2:", element)
# Slicing: Accessing a subarray  (start_row:end_row, start_col:end_col)4
subarray = index_array[0:2, 1:3]  # Accessing rows 0 to 1 and columns 1 to 2
print("\nSubarray:")
print(subarray)

#reshaping and flattening arrays
# Create a 1D array
original_array = np.array([1, 2, 3, 4, 5, 6])
print("\nOriginal 1D Array:")
print(original_array)
# Reshape the array to 2D (2 rows, 3 columns)
reshaped_array = original_array.reshape((2, 3))
print("\nReshaped Array (2x3):")
print(reshaped_array)
# Flatten the array back to 1D
flattened_array = reshaped_array.flatten()
print("\nFlattened Array:")
print(flattened_array)

#mathematical functions on arrays
# Create an array for mathematical functions
math_array = np.array([1, 4, 9, 16, 25])
print("\nOriginal Array for Mathematical Functions:")
print(math_array)
# Square root of each element
sqrt_array = np.sqrt(math_array)
print("\nSquare Root of each element:")
print(sqrt_array)
# Exponential of each element
exp_array = np.exp(math_array)
print("\nExponential of each element:")
print(exp_array)

#mathematical operations on arrays
# Create two arrays for mathematical operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("\nArray A:", array_a)
print("Array B:", array_b)
#addition
addition = array_a + array_b
print("\nAddition (A + B):", addition)
#multiplication
multiplication = array_a * array_b
print("Multiplication (A * B):", multiplication)
#subtraction
subtraction = array_a - array_b
print("Subtraction (A - B):", subtraction)
#division
division = array_a / array_b
print("Division (A / B):", division)


#create 5x5 array of random integers between 1 to 25
random_array = np.random.randint(1, 26, (5, 5))
print("\n5x5 Array of random integers between 1 and 25:")
print(random_array)
#extract last row of the array negative indexing
last_row = random_array[-1, :]
print("\nLast row of the array:")
print(last_row)
#FIRST COLUMN OF THE ARRAY row index is 0 and column index is 0 [:,0] means all rows and first column
first_column = random_array[:, 0]
print("\nFirst column of the array:")
print(first_column)
#sub matrix of containing 3*3
sub_matrix = random_array[1:4, 1:4]
print("\nSub matrix containing 3x3:")
print(sub_matrix)

