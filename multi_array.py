#!/usr/bin/python
import time

a = ([16, 81, 91])
b = ([41, 31])

for x in a:
    for j in b:
        start = time.time()
        p1 = x ** j
        print(str(x) + ' Power ' + str(j) + ' is equal to : '+ str(p1) )
        print((time.time() - start) * 1000)

print('Done')