import numpy as np

# Creating ndarray object and printing in numpy
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))  # numpy.ndarray Type

# Checking version of numpy
print(np.__version__)

# Using tuple to create numpy array
arr2 = np.array((1, 2, 3, 4, 5))

# Dimension in arrays are one-level of depth (nested)
# 0-D array
arr3 = np.array(42)

# 2-D array OR Matrix (An array that has 1-D arrays as its elements)
arr4 = np.array([[1, 2, 3], [4, 5, 6]])

# 3-D arrays have matrices (2D arrays) as their elements 
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# Checking number of dimensions
print(arr5.ndim)  # Output: 3

# Higher dimension arrays
arr6 = np.array([1, 2, 3, 4], ndmin=5)

# Indexing: starts at 0 
print(arr[0])

# Accessing 2D arrays (1st row and second col)
print(arr4[0, 1])

# Using negative indexing to access end of an array
print('Last element from 2nd dim: ', arr4[1, -1])
