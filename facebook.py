#!/usr/bin/python
num = int(input('Enter num : '))
myarray = []
for i in range(num):
    myarray.append("on")
print(myarray)
for j in range(1, num):
    b = j + 1
    for k in range(j, num, b):
        if myarray[k] == "on":
            myarray[k] = "off"
        elif myarray[k] == "off":
            myarray[k] = "on"
    print(myarray)
print('count of on : ', myarray.count('on'))
print('count of off : ', myarray.count('off'))


