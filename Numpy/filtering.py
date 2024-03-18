import numpy as np

# Filtering Numpy Arrays with Boolean index Lists

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

# x = [True, True, False, False, False, False, False, False, False, False]

# print(np1)
# print(np1[x])


'''
filtered = []

for thing in np1:
    if thing % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)


        
print(np1)
print(filtered)
print(np1[filtered])

'''

# Above process is long. Let's use a shortcut

filtered = np1 % 2 == 0

print(np1)
print(filtered)
print(np1[filtered])
