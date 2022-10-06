#!/usr/bin/python
import json
inputfile ="c1.json"
f = open(inputfile, "r", encoding='utf-8-sig')
data = json.load(f)
# auth_count = dict() # Declare empty Dictionar
auth_count = {} # Declare empty Dictionary (Above line also works)
for each in data['values']:
    auth1 = each['author']
    var1 = auth1['raw']
   # print(var1)
    if var1 in auth_count:
        auth_count[var1] += 1
    elif var1 not in auth_count:
        auth_count[var1] = 1

print(auth_count)
f.close()