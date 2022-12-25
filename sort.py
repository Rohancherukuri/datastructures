# Sorting a list or any collection
import numpy as np

l = [27,3,4,9,12,19,1,7,5,23,8,21]
mylist = [int(i) for i in input("Enter a number: ").split(",")]
s = np.sort(l)
print(s)
print(np.sort(mylist))
