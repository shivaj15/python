#!/usr/bin/python
import random
def create_array():
    my_array = []
    for i in range(8):
        my_array.append(random.randrange(1, 20))
    return my_array

a = create_array()
print(a)
array_sum = 0
for i in a:
    array_sum += i
if array_sum % 2 == 0:
    print("Array sum : ", array_sum, "is even, proceeding")
else:
    print("Array sum : ", array_sum, "is not even, proceeding with new array")

