# The input is arr [17,18,5,4,6,1]. Ouptut is [18,6,6,6,1,-1]
# Trying to find the number further in the list bigger than current number. 

# Solution 1 with nested for loop.
arr = [17,18,5,4,6,1]
# Output list
l = []

for i in arr:
    # big is the comparison value 
    big = 0
    # After the index of this value, iterate over those values. 
    for r in arr[arr.index(i)+1:]:
        # If this new value is bigger than the comparison value, then make this new value the comparison value. 
        if r>big: big = r
    if big != 0:l.append(big)

    # If none of the elements after is bigger, input nothing. It usually happens in the last value.
        
l.append(-1)
# Input -1 for the last value. 
print(l)



