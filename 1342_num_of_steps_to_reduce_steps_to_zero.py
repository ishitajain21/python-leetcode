# Input: 14 Output: 6 
# This program takes a number and calculates how many steps it takes to get to 0. A "step" is either subratcting 1 or dividing by 2. 

# The variable that counts how many steps it takes to get to 0. 
count =  0


def count_steps(num):
    # Makes the variable global so that the the count can be accesed and changed. 
    global count 
    if num == 0 :
        # This is the base case of the recursive function. 
        print(count)
    elif num %2 == 0:
        # If the num can be divisible by 2, add 1 to count and divide the num by 2. 
        count += 1
        num = num/2
        # Go through the code again. 
        count_steps(num)
    else:
        # It means that the 1 will have to be subtracted from the num. 
        count += 1
        num -= 1
        count_steps(num)

count_steps(14)
