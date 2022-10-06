#!/usr/bin/python
import random
def create_array():
    my_array = []
    for i in range(6):
        my_array.append(random.randrange(1, 10))
    return my_array

a = create_array()
print(a)

max_area = 0
for i in range(len(a)):
    b = i + 1
    while b < len(a):
        if a[i] < a[b]:
            min_val = a[i]
        else:
            min_val = a[b]
        index_val = b - i
        area = min_val * index_val
        if area > max_area:
            max_area = area
            ind_1 = i
            ind_2 = b
        b += 1
print("Max area = ", max_area)
print("Index values : ", ind_1, ind_2)
