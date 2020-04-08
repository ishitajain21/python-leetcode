# Input: [555,901,482,1771]. Output: 1.
# Find the number of elements in the list that has an even number of elements. 

# The list that serves as the input. 
nums = [555,901,482,1771]
# The variable that stores the number of elements that have an even number of digits. 
count = 0 

for i in nums:
    # Go through the list and convert the element to a string. 
    i = str(i)
    # If the length of the string is divisible by 2, it means it has even number of characters. 
    if len(i)%2 == 0:
        # Add one to the count variable 
        count +=1 
print("There are",count,"elements in the list with an even number of digits.")
