#!/usr/bin/python3

# my_arraysize = int(input("Enter the array size: "))
# my_array = []
# for i in range(0, my_arraysize):
#    my_array.append(int(input()))

my_array = [13, 24, 65, 21, 5, 9, 100, 78, 62, 20, 19, 89, 15, 28]
# print (my_array)
my_array_len = len(my_array)
k = 6

for i in range(0, k ):
    l = i + 1
    for j in range( l, my_array_len):
        if my_array[i] > my_array[j]:
            my_array[i], my_array[j] = my_array[j], my_array[i]

    print(my_array)
print(my_array[k - 1])




