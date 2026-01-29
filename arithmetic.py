import numpy as np

# Scalar Arithmetic

# radii = np.array([1, 2, 3])
#
# print(array + 1)
# print(array * 2)
#
#
# # vectorized Math function
#
# print(np.sqrt(array))
# print(np.round(array))
# print(np.pi)

#
# excercise

# print(np.pi * radii ** 2)


array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 ** array2)
print(array1 % array2)
print(array2 / array1)
print(array2 // array1)


# comparision operators

scores = np.array([23, 32, 54, 65, 75, 88, 99])


scores[scores < 60] = 0
print(scores)


