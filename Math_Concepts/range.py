import numpy as np

data =  [1200, 1500, 3400, 4444]
minimum = min(data)
maximum = max(data)
range_value = maximum - minimum

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_value}")
print(f"Mean: {(minimum + maximum) / 2}")
print(f"Median: {data[2]}")
print(f"Mode: {max(set(data), key=data.count)}")
print(f"Standard Deviation: {round(np.std(data), 2)}")
print(f"Variance: {round(np.var(data), 2)}")
print(f"Sum: {sum(data)}")
print(f"Product: {np.prod(data)}")


