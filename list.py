#!/usr/bin/python

#this is a simple list program

mylist1 = ['a', 'b', 3, 'x', 'siv']
mylist2 = [1, 4, 5, 8, 'hello']
mylist3 = [ 1, 1, 2, 2, 'x', 'y', 'x']
print("printing complete mylist 2 : ", mylist2)        # prints entire list mylist2
print()
print(mylist1[2], '\n')    # prints 3 from mylist1 , counting start from 0
print(mylist1[2:], '\n')   # prints 2, x , siv from mylist1, prints from #2 to end of the list
print("printing mylist1 elements 1 to 4 :", mylist1[1:4])

mylist2[4] = 'Hello world' # Update list value
mylist2.append('New') # append list value

print("Printing mylist2 length :", len(mylist2))
print(mylist2, '\n')
print("Printing mylist2 length after append:", len(mylist2))
mylist2.remove(5) # removes value 5 from the list
print("Printing mylist2 & length after remove:", mylist2, len(mylist2))
mylist3.remove(2)
print(mylist3)
# print(mylist3.pop())
mylist3.pop(3)
print(mylist3)
del mylist3[1]   # delete second element
print(mylist3)
del mylist3[1:3]   # delete index values 1 & 2 only,Third item not deleted
print(mylist3)
