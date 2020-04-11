# Input: user given(s) Output: Lower case of (s)
# Example: Input: "hElOW" Ouput: helow
s = input("What is the string?")

# Easy way: 
#The easy way because python has a built-in function that can lower-case. 

print(s.lower())

# Hard Way:
# Another solution without using the function. 

# The end string that has all lower case letters. 
lower_case_string = ""

dic = {"Q" :"q","W" :"w","E" :"e","R" :"r","T" :"t","Y" :"y","U" :"u","I" :"i","O" :"o","P" :"p","A" :"a","S" :"s","D" :"d","F" :"f","G" :"g","H" :"h","J" :"j","K" :"k","L" :"l","Z" :"z","X" :"x","C":"c","V" :"v","B" :"b","N" :"n","M" :"m"}

for i in s:
    # For every element in the string. 
    try:
        n = dic[i]
        # n is the key of the i. The key is siply the lower case of i. 
        lower_case_string += n 
        # Add the newly lower cased letter to the end string. 
    except:
        # However, all letters won't be capital letters. In that case, add the element just as it is to the end string. 
        lower_case_string += i

print(lower_case_string)
