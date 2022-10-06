#!/usr/bin/python

mylist = [['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'] ]
finalList = []

x = int(len(mylist[0]))
y = int(len(mylist))


for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(mylist[j][i])
    finalList.insert(i, tmp)


for i in range(len(mylist)):
    print(mylist[i])

for i in range(len(finalList)):
    print(finalList[i])

'''
def createlist(x, y):
    tmp = []
    for i in range(y):
        tmp.append(mylist[i][x])
    return tmp


for i in range(x):
    tmp = createlist(i, y)
    finalList.insert(i, tmp)


for i in range(len(mylist)):
    print(mylist[i])

for i in range(len(finalList)):
    print(finalList[i])

'''
