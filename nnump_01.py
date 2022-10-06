#!/usr/bin/python
import time

import numpy
import numpy as np
x = np.array([23, 45, 12, 4, 7, 99, 78, 20])

y = x[np.argsort(x)[::-1][-2:]]

print(y)


a = ([2,3,6,8,9,23,45,65,31,9,56,13,89,92,36,27])
m = a[::-1]
print("printing " + str(m) )
print(str(m))
newnp = np.array(a)
b = numpy.argsort(a)  # Prints only sorted array index
print(b)
b = newnp[numpy.argsort(a)] # calls the newnp with sorted index value and returns the sorted array values
print(b)
b = b[::-1][-2:]
print(b)

size = 100000
l1 = range(size)
l2 = range(size)
l3 = np.arange(size)
l4 = np.arange(size)


start = time.time()
l6 = l3 + l4
print(l6 + "Numpy")
print((time.time() - start )* 1000)

start = time.time()
l5 = [(x,y) for x, y in zip(l1,l2) ]
print("l5" + "List")
print((time.time() - start) * 1000)

