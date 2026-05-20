#creating array from list
import numpy as np

list1 = [1, 2, 3, 4, 5]
arr1d = np.array(list1)
print("1D Array from list:")
print(arr1d)

#creating array from tuple
tuple1 = (6, 7, 8, 9, 10)
arr1d_tuple = np.array(tuple1)
print("\n1D Array from tuple:")
print(arr1d_tuple)

#creating array from nested list
nested_list = [[1, 2, 3], [4, 5, 6]]
arr2d = np.array(nested_list)
print("\n2D Array from nested list:")
print(arr2d)


#creating array from nested tuple
nested_tuple = ((7, 8, 9), (10, 11, 12))
arr2d_tuple = np.array(nested_tuple)
print("\n2D Array from nested tuple:")
print(arr2d_tuple)