import numpy as np

array = np.array([[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']],
                [['M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T'], ['U', 'V', 'W', 'X']],
                [['Y', 'Z', '1', '2'], ['3', '4', '5', '6'], ['7', '8', '9', '0']]])

print(array.shape)
print(array[1][2][2])
#chain indexing

yo = array[1,1,1] + array[1,2,0] + array[1,0,3] + array[0,1,0] + array[1, 1, 2] + array[0,1,3] #preferred indexing
print(yo)

one_dimensional_arr = np.array([10, 12])
print(one_dimensional_arr)

two_dimensional_arr = np.array([[10, 12], [13, 14]])
print(two_dimensional_arr)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)


lin_spaced_arr = np.linspace(0, 100, 5, dtype=float)
print(lin_spaced_arr)


# Return a new array of shape 3, filled with ones.
ones_arr = np.ones(3)
print(ones_arr)


# Return a new array of shape 3 with random numbers between 0 and 1.
rand_arr = np.random.rand(3)
print(rand_arr)

two_dimensional = np.array([[[1, 2, 3], [4, 5, 6]]])
print(two_dimensional)

three_dimensional = np.array([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])
print(three_dimensional)



# 1-D array
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])

# Multidimensional array using reshape()
multi_dim_arr = np.reshape(
                one_dim_arr, # the array to be reshaped
               (2,3) # dimensions of the new array
              )
# Print the new 2-D array with two rows and three columns
print(multi_dim_arr.ndim)


vector = np.array([1, 2, 3])
print(vector * 3)


# Indexing on a 2-D array
two_dim = np.array(([1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]))

# Select element number 8 from the 2-D array using indices i, j.
print(two_dim[2][1])



a1 = np.array([[1,1],
               [2,2]])
a2 = np.array([[3,3],
              [4,4]])
print(f'a1:\n{a1}')
print(f'a2:\n{a2}')

# Stack the arrays vertically
vert_stack = np.vstack((a1, a2))
print(vert_stack)

horz_stack = np.hstack((a1, a2))
print(horz_stack)

# Create a 3-D array
three_d_array = np.array([[[1, 2], [3, 4]],
                          [[5, 6], [7, 3]]])
print(three_d_array)






