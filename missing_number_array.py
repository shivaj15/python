#!/usr/bin/python3

my_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

l = len(my_array) - 1
for i in range(0, l):
    j = i + 1
    if j != my_array[i]:
        print("Missing number : ", j)
        break
