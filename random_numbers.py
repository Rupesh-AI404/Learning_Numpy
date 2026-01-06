import numpy as np

rng = np.random.default_rng(seed = 5)  #seed is the random number generator

print(rng.integers(1, 100, size = 3))  #generate 10 random integers between 1 and 100 with the size of 3


print(np.random.uniform(1.0, 5.0, size = (2, 3)))  #generate random float numbers between 1.0 and 5.0 with the size of 2x3 array


rng = np.random.default_rng()

fruits = np.array(['apple', 'banana', 'cherry', 'coconut', 'date', 'elderberry', 'fig'])
fruits = rng.choice(fruits, size = (2,3), replace = False)

print(fruits)

players = np.array(['Alice', 'Bob', 'Charlie', 'David'])
rng.shuffle(players)
print(players)

