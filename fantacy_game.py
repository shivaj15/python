#!/usr/bin/python

usrDict = {'rope': 1, 'tourch': 6, 'gold coin' : 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'ruby', 'gold coin', 'rope', 'gold coin']

def displayInventory(dict):
    print('Inventory :')
    totalItems = 0
    for key, val in dict.items():
        print(str(val) + '\t' + key)
        totalItems +=  val
    print('Total Items = ' + str(totalItems))

def addInventory(dragonLoot, dict):
    for item in dragonLoot:
        if item in dict.keys():
            dict[item] = dict[item] + 1
        elif item not in dict.keys():
            print('Processing item : ' + item)
            dict[item] = 1
'''
def f2(dict):
    print('Inventory : (from F2) ')
    for key in dict.keys():
        print(str(dict.get(key)) + '\t' + key)
'''

displayInventory(usrDict)
addInventory(dragonLoot, usrDict)
displayInventory(usrDict)
