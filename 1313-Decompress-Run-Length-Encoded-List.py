# Input: [1,2,3,4] Output: [2,4,4,4]
# The first element tells the frequency and the next element tells the number. 
nums = [1,2,3,4]

#The output list. 
l = []

# Stores the even elements. 
freq = 0 

for i in nums:
    # Checks if the number is of an odd or even index. 
    # Even index elements all tell the frequency while Odd index are the elements.
    if nums.index(i)%2 == 1:
        # Make the frequency of the element. 
        for j in range(0,freq): 
            # Put that in the output list. 
            l.append(i)
    if nums.index(i)%2 ==0:
        # Updatae the frequency of the element to that new one. 
        freq = i
print(l)
