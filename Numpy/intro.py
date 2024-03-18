import numpy as np

list1 = [1, 2, 3, 4, 5]

list2 = ["John Elder", 41, list1, True]

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)
print(np1.shape)

# Range
np2 = np.arange(10)
print(np2)

# Stop

np3 = np.arange(0, 10, 2)
print(np3)

# Zeros
np4 = np.zeros(10)
print(np4)

#Multidimensional Zeros

np5 = np.zeros((2, 10))
print(np5)

# Full
np6 = np.full((10), 6)
print(np6)

# Multi dimensional full

np7 = np.full((2, 10), 6)
print(np7)

# Converting a python list to a Numpy

list3 = [1, 2, 3, 4, 5]

np8 = np.array(list3)
print(np8)