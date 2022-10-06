#!/usr/bin/python
num = int(input('Enter num : '))
myarray = []
for i in range(num):
    myarray.append("x")
print(myarray)
for j in range(1, num):
    b = j + 1
    for k in range(j, num, b):
        if myarray[k] == "x":
            myarray[k] = "y"
        elif myarray[k] == "y":
            myarray[k] = "x"
    print(myarray)
print('count of y : ', myarray.count('y'))
print('count of x : ', myarray.count('x'))
