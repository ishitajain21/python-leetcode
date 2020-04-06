
nums = [1,2,3,4]
l = []

freq = 0 


for i in nums:
    if nums.index(i)%2 == 1:
        for j in range(0,freq): 
            l.append(i)
    if nums.index(i)%2 ==0:
         freq = i
print(l)
