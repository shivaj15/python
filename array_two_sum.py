#!/usr/bin/python
import random
array_size = int(input("Enter the array length : "))
total_value = int(input("Enter the total value : "))
my_array = []
my_index = []
for i in range(array_size):
    my_array.append(random.randrange(1, 20))

for i in my_array:
    #print(i)
    if total_value >= i:
        target_value = total_value - i
        if i in my_index:
            print("match found for :", i)
            break
        if target_value not in my_index:
            print(target_value)
            my_index.append(target_value)
            #elif target_value in my_index:
# print("no match found")

print("\n \n")
print(my_array)