#14, 7, 6, 3,2,1  
# 16,8,4,2,0

import sys

count =  0

def count_steps(num):

    count =0
    if num==0:
        return count
    else:
        count+=1
        while num>0:
            test(num)

def test(inc):
    global count 
    if inc == 0 :
        print(count)
        sys.exit()
    if inc %2 == 0:
        count = count + 1
        inc = inc/2
        test(inc)
    else:
        count += 1
        inc = inc - 1
        test(inc)

test(14)
