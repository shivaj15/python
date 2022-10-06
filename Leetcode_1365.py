#!/usr/bin/env python3

# Leet Code : 1365. How Many Numbers Are Smaller Than the Current Number


'''Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100

'''

import random

arrayLength = random.randrange(3, 100)
print('Array Size : ' + str(arrayLength))
inputArray = []
for i in range(arrayLength):
    inputArray.append(random.randrange(1, 100))

print(inputArray)
outputArray = []
for j in inputArray:
    count = 0
    for k in range(0, arrayLength):
        if j > inputArray[k]:
            count += 1

    outputArray.append(count)

print(outputArray)


