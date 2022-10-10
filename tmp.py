#!/usr/bin/python
#num = int(input("Enter value: "))
abc = 200
num = int(abc)
list = []

for i in range(num):
    list.append(1)


for j in range(1, num):
    for k in range(j, num, j+1):
        if list[k] == 1:
            list[k] = 0
        else:
            list[k] = 1

print("On Switch : " + str(list.count(1)))


