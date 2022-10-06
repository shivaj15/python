#!/usr/bin/python

number = int(input("Enter the number : "))

def collatz(number):
    if (number % 2 == 0):
        number = number // 2
        return number
    elif (number % 2 == 1):
        number = number * 3 + 1
        return number
    else:
        print("Number error")

while (number != 1):
    print(number)
    number = collatz(number)

print(number)