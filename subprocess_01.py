#!/usr/bin/env python
import subprocess

a = range(10)
f = open('test1.txt', 'w')
for i in a:
    f.write('Hello : ' + str(i) + '\n')

for i in a:
    x = subprocess.run(['ls', '-l', f'{i}' ], stdout=subprocess.DEVNULL, stderr=f)

f.close()
