#!/usr/bin/python

search_text = "test"
replace_text = "Replace TESTED"


with open(r'testfile.txt', 'r+') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
    file.write(data)


print("Text replaced")