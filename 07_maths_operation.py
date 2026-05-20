#math operations
import numpy as np

# Create a 1D array
arr1d = np.array([10, 20, 30, 40, 50])
print("Original Array:")
print(arr1d)
print(arr1d+5)  # Add 5 to each element
print(arr1d*2)  # Multiply each element by 2
print(arr1d-3)  # Subtract 3 from each element
print(arr1d/2)  # Divide each element by 2
print(np.sqrt(arr1d))  # Square root of each element
print(np.exp(arr1d))  # Exponential of each element
print(np.log(arr1d))  # Natural logarithm of each element
print(np.sin(arr1d))  # Sine of each element
print(np.cos(arr1d))  # Cosine of each element

# Create two 1D arrays
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("Array A:", array_a)
print("Array B:", array_b)

# Addition
addition = array_a + array_b
print("\nAddition (A + B):", addition)

# Multiplication
multiplication = array_a * array_b
print("Multiplication (A * B):", multiplication)

# Subtraction
subtraction = array_a - array_b
print("Subtraction (A - B):", subtraction)

# Division
division = array_a / array_b
print("Division (A / B):", division)

# Create a 5x5 array of random integers between 1 and 25
random_array = np.random.randint(1, 26, (5, 5))
print("\n5x5 Array of random integers between 1 and 25:")
print(random_array)
# Extract the last row of the array using negative indexing
last_row = random_array[-1, :]  # ()
print("\nLast row of the array:")
print(last_row)