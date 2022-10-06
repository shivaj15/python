#!/usr/bin/python

def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


my_list = [1,2,3,4,-2,4,-1]
a = multiply(my_list)
print(a)