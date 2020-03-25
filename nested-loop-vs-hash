# This file has 2 different parts. Part A is the hash table solution to the smaller Numbers than current numbers in leet code.
# It will output the time it takes to solve the problem. Change the variable x to see how the time changes. 


import random 
import time 

l = []
for i in range(0,8000):
# The 8000 was the x position. Change it to see the difference in time. 
  r = random.randint(0,100)
  l.append(r)

name = "ishita"
def smallerNumbersThanCurrent(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start_time = time.time()
        d = {}
        for idx, val in enumerate(sorted(nums)):
            if val not in d:
                d[val] = idx
        res = []
        for i in nums:
            res.append(d[i])
        end_time = time.time()
        print(end_time-start_time, "seconds")   
        return res




smallerNumbersThanCurrent(l)


# This is option 2 which uses the nested for loop to solve the same problem. 

import random
import time
l = []
for i in range(0,500):
# The 500 is the x. Change it to see how the time changes. 
  r = random.randint(0,100)
  l.append(r)

out = []
def small(nums):
  start_time = time.time()
  for n in nums: 
    count = 0 
    for i in nums:
      if n != i and n>i:
        count=count+1
    out.append(count)
  end_time = time.time()
  print(end_time-start_time, "seconds")
  return out
small(l)



