#!/usr/bin/python

# VERIFIED - SIMPLEY WORKING FINE:
import json

f = open('sample4.json')
data = json.load(f)
for each in data['people']:
    print(each) # Prints the entire dictionary line
    print(each["lastName"]) # Prints the "lastName key" value from the dictionary
    print(each["firstName"], each["lastName"])  # Prints the "firstName key" &"lastName key" value from the dictionary
f.close()
