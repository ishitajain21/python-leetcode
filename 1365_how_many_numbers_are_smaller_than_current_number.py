# This code has 2 different solutions to this problem in leetcode. However, my main objective in this was to see the time it took to complete this code when I change how many elements it had to process.  
# To see how long it takes to complete these two change the value when the comment says to. 

# Independent Var: The number elements that the code will process to get to the output. 
# Dependent Var: The time it takes for the code to process the independent var.
# Control: Range of elements. List that goes through the 2 solutions. 
# Cases: Solution 1 and Solution 2 

# Solution 1: 
# We need random so that we can generate random values. 
import random 
import time 

l = []
# This code will generate random elements as input. 
for i in range(0,8000):
# The 8000 is how many elements are generated to test. Change it to see how long it takes for the code to run thorugh. 
  r = random.randint(0,100)
  l.append(r)


def solOne(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Starts the time:
        start_time = time.time()
        # The dictionary way I use. 
        d = {}
        for idx, val in enumerate(sorted(nums)):
            if val not in d:
                d[val] = idx
        res = []
        for i in nums:
            res.append(d[i])
        end_time = time.time()
        print("Solution 1 time:", end_time-start_time, "seconds")   
        return res

solOne(l)


# Solution 2:

out = []
def solTwo(nums):
  start_time = time.time()
  for n in nums: 
    count = 0 
    for i in nums:
      if n != i and n>i:
        count=count+1
    out.append(count)
  end_time = time.time()
  print("Solution 2 time:",end_time-start_time, "seconds")
  return out

solTwo(l)



