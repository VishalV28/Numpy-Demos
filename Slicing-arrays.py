# Slicing means taking elements from one given index to another given index.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# We pass slice instead of index like this: [start:end] 
print(arr[1:5])  # 2,3,4,5 (includes start index and discludes end index)

# If we don't pass start its considered 0
print(arr[:4])

# If we don't pass end its considered length of array in that dimension
print(arr[3:])

# Negative slicing
print(arr[-3:-1])

# We can also define the step, like this: [start:end:step].
# If we don't pass step its considered 1
print(arr[1:5:2]) # every other element in specified bounds
print(arr[::2])   # every other element from entire array

# Slicing 2D arrays
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])  
print(arr[0:2, 2])   # From both elements, return index 2
print(arr[0:2, 1:4]) # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array

