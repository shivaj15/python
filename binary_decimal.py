#!/usr/bin/env python

import re
import sys
binInput = str(input('Enter a binary number : '))


def bitCheck(binInput):
    regPatern = re.compile(r"[^01]")
    for digit in binInput:
        searchResult = re.search(regPatern, digit)
        if searchResult != None:
            print("Enter Binar numbers Only (ie 0 or 1) : ")
            sys.exit(1)

    print("Converting Binary number " + binInput + " to Decimal umber")

def convertDecimal(binInput):
    binNumlist = list(binInput)
    reversedList = reversed(binNumlist)
    power = 0
    decimalNum = 0
    for num in reversedList:
        i = int(num)
        decimalNum = decimalNum + ( i * (2 ** power))
        power += 1
    return decimalNum

bitCheck(binInput)
result = str(convertDecimal(binInput))

print("Decimal number : " + result )



