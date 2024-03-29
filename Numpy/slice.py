import numpy as np

# Slicing numpyy Arrays

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Return 2,3,4,5
print(np1[1:5])

# Return from something till the end of the array
# 4 - 9
print(np1[3:])

# 7 - 8
print(np1[-3:-1])

# Steps

print(np1[1:5]) # 2- 5

print(np1[1:5:2]) # 2-5 in 2 steps

# Steps on the entire array

print(np1[::2])

print(np1[::3])

# Slice a 2D Array

np2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Pull out a single item
print(np2[1,2]) # The 1 here is the second array and 2 is the 0,1,2th item in the second array([6,7,8,9,10])

# Slice a 2-D Array

print(np2[0:1, 1:3]) # Gives 2,3

# Slice from both rows

print(np2[0:2, 1:3])