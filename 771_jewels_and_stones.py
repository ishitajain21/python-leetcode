# Input: Jewel: aA Stone: aAAbbb. Output: 2 
def jas(s,j):
    #J is the type of stones that are jewels
    # S is the stones ypy have, 
    # You want to know how many characters in S are in J. No repeats. 
    count = 0 
    
    for x in s:
        if x in j:
            # adds one to the count
            count+= 1
            # deletes all instances of that variable so that it isn't counted again. 
            s.replace(x,"")
            j.replace(x,"")
            
    return count

print(jas("aA","aAAbbb"))
