#!/usr/bin/python
import random, datetime
num = int(input("Enter the value : "))
my_list = []
for i in range(1, num):
    rn = random.choice(range(1,999))
    my_list.append(rn)
my_list1 = my_list.copy()
my_list2 = my_list.copy()
print(my_list1)
#my_list[0],my_list[1] = my_list[1],my_list[0]
#print(my_list)

start_time = datetime.datetime.now()
print("Sorting begins : ", start_time )
for i in range(1, len(my_list1)):
    j = i - 1
    if my_list1[i] < my_list1[j]:
        my_list1[i], my_list1[j] = my_list1[j], my_list1[i]
    while j >= 1:
        k = j - 1
        if my_list1[j] < my_list1[k]:
            my_list1[j], my_list1[k] = my_list1[k], my_list1[j]
        else:
            break
        j -= 1

end_time = datetime.datetime.now()
print("my_list1 sorted : ", my_list1)
print('Executio time %s {}'.format(end_time - start_time))

