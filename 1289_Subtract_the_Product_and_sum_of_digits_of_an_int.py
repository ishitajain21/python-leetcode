# Input: "13" Output: -1
# Takes the sum of the digits of the number and subtracts it from the product of the digits.

#Takes the number input from the user as a string.
num = input("What is the number?") 

# Exception handling
try:
    #The list that will house the digits of the number.
    digits = []

    #Since the input is a string, this for loop will extract each individual digits and append it to digits.
    for i in num:
        digits.append(i)

    # These next 2 variables are to store the sum and product of the digits, respectively.
    sumi = 0 
    prod = 1
    # The for loop will add or multiply the digit to the variable. 
    for i in digits:
        i = float(i)
        sumi += i
        prod *= i 
    # Prints the difference between the product and the sum 
    print(prod-sumi)
except ValueError:
    print("Please enter an integer!")
