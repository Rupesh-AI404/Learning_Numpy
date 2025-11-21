import numpy as np

array = np.array([[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']],
                [['M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T'], ['U', 'V', 'W', 'X']],
                [['Y', 'Z', '1', '2'], ['3', '4', '5', '6'], ['7', '8', '9', '0']]])

print(array.shape)
print(array[1][2][2]) #chain indexing

yo = array[1,1,1] + array[1,2,0] + array[1,0,3] + array[0,1,0] + array[1, 1, 2] + array[0,1,3] #preferred indexing
print(yo)




