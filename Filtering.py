import numpy as np

#Filtering: It refers to the process of selecting element from an array that match a given condition

ages = np.array([[21, 32, 43, 54, 18, 23, 34, 45, 56, 65],
                 [12, 23, 34, 45, 56, 67, 78, 89, 90, 10]])

teenagers = ages[ages <= 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
veryYoung = ages[ages < 12]

adult = np.where(ages >= 18, ages, 0)  #if age >= 18, keep age, else set to 0
print(adult)

print(adults)
print(teenagers)
print(seniors)
print(evens)
print(odds)
print(veryYoung)
