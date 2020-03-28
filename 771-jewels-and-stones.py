
def jas(s,j):
    #J is the type of stones that are jewels
    # S is the stones ypy have, 
    # You want to know how many characters in S are in J. 
    count = 0 
    l = []
    for i in j:
        l.append(i)
    for x in s:
        if x in l:
            count+= l.count(x)
            
    return count

print(jas("aA","aAAbbb"))
