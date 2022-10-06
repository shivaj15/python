#!/usr/bin/python
import random, string
num = int(input("Enter N value : "))
my_list = []
for i in range(num):
    a = random.choice(string.ascii_uppercase)
    my_list.append(a)

my_set = set(my_list)

print(my_list)
print(my_set)