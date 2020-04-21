# WIth an input only filled with 6s and 9s, replace only 1 number to make it the maximum number possible. 
num = input("What is the number?")
# INput: 6699, Output: 9699
num = num.replace("6","9",1)
# Replace the first instance of "6" with "9" to make it the max number. 
print(num)
