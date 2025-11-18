import numpy as np


#Aggregate Functions = summarize data and typically returns a single value

aggregate_functions = {
    "sum": np.sum,     #to sum all the elements in the array
    "mean": np.mean,   #to find the mean of all the elements in the array
    "median": np.median,#to find the median of all the elements in the array
    "min": np.min,      #to find the minimum value in the array
    "max": np.max,      #to find the maximum value in the array
    "std": np.std,      #to find the standard deviation of all the elements in the array
    "var": np.var,      #to find the variance of all the elements in the array
    "prod": np.prod,    #to find the product of all the elements in the array
    "all": np.all,      #to check if all the elements in the array are True
}

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

print(np.sum(array))
print(np.mean(array))
print(np.median(array))
print(np.min(array))
print(np.max(array))
print(np.std(array))
print(np.var(array))
print(np.prod(array))
print(np.all(array))
print(np.any(array))  #to check if any of the elements in the array are True

print("axis = 0 is row-wise sum")
print(np.sum(array, axis=0))  #row-wise sum

print("axis = 1 is column-wise sum")
print(np.sum(array, axis=1))  #column-wise sum

#You can also use the aggregate functions dictionary to call the functions
for func_name, func in aggregate_functions.items():
    print(f"{func_name}: {func(array)}")

for func_name, func in aggregate_functions.items():
    print(f"{func_name} (axis=0): {func(array, axis=0)}")