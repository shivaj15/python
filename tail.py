#!/usr/bin/env python
import pprint
inputFile = open('sample2.txt', 'r')

# linesPrint = input ('Enter the line to print : ')

lines = inputFile.readlines()
totalLine = len(lines)
print('Total Line = ' + str(totalLine))
lineToPrint = totalLine - 10

for i in range(lineToPrint, totalLine):
    print(lines[i], end='')
