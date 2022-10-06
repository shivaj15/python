#!/usr/bin/python
import json
import pprint
#f = open('c1.log', "r", encoding='utf-8-sig')
f = open('c1.json')
data = json.load(f)
for key, val in data.items():
    print(key, ":", val)
