#!/usr/bin/python

a = int(1)
b = int(2)
c = int(3)
d = int(4)
e = int(5)

file = open("test.txt", "w")
for i in range(1, 5):
    file.write(a + b + c)

file.close()