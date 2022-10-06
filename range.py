#!/usr/bin/python

mylist1 = list(range(5))
print(mylist1)
mylist2 = list(range(2, 5))
print(mylist2)
mylist3 = list(range(2, 15, 3))  # seq increment value 3
print(mylist3)

samplelist = list(range(0,100,20))
for i in samplelist:
#   mod = i % 8
    if (i % 8) == 0:
        print(i, ": is divisible by 8")
    else:
        print(i, ": is not divisible by 8")
