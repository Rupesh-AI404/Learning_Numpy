import numpy as np

# print(np.__version__)  (to check the version of the numpy library)

my_list = [1, 2, 3, 4]


my_list = my_list * 2
print("Original list:", my_list)

array = np.array([1, 2, 3, 4])
array = array * 5
print(array)
print(type(array))
