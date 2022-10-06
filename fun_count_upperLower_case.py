#!/usr/bin/python

my_string = input("Enter the string : ")

def caseCounter(my_data):
    counter = {"Upper_Case": 0, "Lower_Case": 0}
    for char in my_data:
        if char.isupper():
            counter['Upper_Case'] += 1
        elif char.islower():
            counter['Lower_Case'] += 1
        else:
            pass
    print("Upper Case : ", counter['Upper_Case'])
    print("Lower Case : ", counter['Lower_Case'])
caseCounter(my_string)