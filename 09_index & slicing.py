import numpy as np

#create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)  # Output: [1 2 3 4 5]

#accessing elements
print(arr1d[0])  # Output: 1
print(arr1d[2])  # Output: 3
print(arr1d[-1])  # Output: 5 


#slicing  (start:stop:step)
print(arr1d[1:4])  # Output: [2 3 4]
print(arr1d[:3])  # Output: [1 2 3]
print(arr1d[3:5])  # Output: [4 5]
print(arr1d[::2])  # Output: [1 3 5] (step of 2, every second element)
print(arr1d[::-1])  # Output: [5 4 3 2 1] (reverses the array)


#slicing with negative indices (start:stop:step)
print(arr1d[-4:-1])  # Output: [2 3 4]
print(arr1d[-1:])  # Output: [5] (last element)
print(arr1d[:-2])  # Output: [1 2 3] (all elements except the last two)


#fancy indexing (using a list of indices)
arr1d = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr1d[indices])  # Output: [10 30 50] 



#boolean indexing (using a condition)
arr1d = np.array([10, 20, 30, 40, 50])
condition = arr1d > 25
print(arr1d[condition])  # Output: [30 40 50] (elements greater than 25)


# Create a 2D array for indexing and slicing [row_start:row_stop, col_start:col_stop]
arr2d = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

# Indexing: Accessing a specific element
print(arr2d[0])  #same as arr2d[0, :]  # Output: [10 20 30] (first row)
print(arr2d[1])  # Output: [40 50 60] (second row)
print(arr2d[:, 0])  # Output: [10 40 70] (first column)
print(arr2d[:, -1])  # Output: [30 60 90] (last column)
print(arr2d[0, :])  # Output: [10 20 30] (first row)
print(arr2d[1, 1])  # Output: 50 (second row, second column)


#slicing 

print(arr2d[1:3, 0:2])  # Output: [[40 50] [70 80]] (slicing a subarray)
print(arr2d[0:2, 1:3])  # Output: [[20 30] [50 60]] (slicing rows 0 to 1 and columns 1 to 2)
print(arr2d[::2, ::2])  # Output: [[10 30] [70 90]] (slicing every second row and column)
print(arr2d[::-1, ::-1])  # Output: [[90 80 70] [60 50 40] [30 20 10]] (reversing the array)





# Create a 3D array for indexing and slicing [block_start:block_stop, row_start:row_stop, col_start:col_stop]
arr3d = np.array([[[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9], 
                   [10, 11, 12]]])


# Indexing: Accessing a specific element
print(arr3d[0, 0, 0])  # Output: 1 (first block, first row, first column)
print(arr3d[0, 1, 2])  # Output: 6 (first block, second row, third column)
print(arr3d[0, 2])  # Output: [[7 8 9] [10 11 12]] (first block, third and fourth rows)
print(arr3d[0, :, 1])  # Output: [2 5 8 11] (first block, all rows, second column)
print(arr3d[0, :, :-1])  # Output: [[3 2 1] [6 5 4] [9 8 7] [12 11 10]] (first block, all rows, columns in reverse order)