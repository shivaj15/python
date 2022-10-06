#!/usr/bin/env python
import sys

decimalNum = (input("Enter a decimal number: "))

binList = []


def numCheck(decimalNum):
    try:
        decimalNum = int(decimalNum)
    except ValueError:
        print("Enter a valid integer value:")
        sys.exit(1)
    if decimalNum > 0:
        print("Coverting number " + str(decimalNum) + " to binary :")
    else:
        print("Try with valid integer value")
        sys.exit(1)

def numConvert(numInput):
    numInput = int(numInput)
    while numInput > 0:
        mod = numInput % 2
        binList.insert(0, mod)
        numInput = numInput // 2
    return binList


numInput = decimalNum

numCheck(decimalNum)
outPut = numConvert(numInput)
print(outPut)