#!/usr/bin/python

match_words = ['mango', 'cat', 'dog', 'apple']
my_dict = dict()
for i in match_words:
    my_dict[i]=0
    print(my_dict)
f = open('sample.txt')
for line in f:
    line = line.strip()
    for word in line.split(" "):
        if word in my_dict:
            my_dict[word] += 1
        print(my_dict)
print(my_dict)
f.close()
