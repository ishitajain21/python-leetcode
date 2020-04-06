num = input("What is the number?") 

digits = []

for i in num:
    digits.append(i)

sumi = 0 
prod = 1
for i in digits:
    i = int(i)
    sumi += i
    prod *= i 

print(prod-sumi)
