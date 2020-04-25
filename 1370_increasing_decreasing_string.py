
# Given a string s. You should re-order the string using the following algorithm:

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algo 

inp = "aaabbbccc"
out_for_check = ""
out = ""

def check_till_everything_is_gone():
    global inp
    global out
    global out_for_check
    if inp == "":
        print(out)
    else:
        pick_char_out()
        repeat_steps()
        check_till_everything_is_gone()

def pick_char_out():
    global out
    global out_for_check
    start = ""
    for i in inp:
        if i not in start: start += i
    out_for_check += start
    out += start + start[::-1]

def repeat_steps():
    global inp
    for i in out_for_check:
        inp = inp.replace(i,"",1)
    
        
check_till_everything_is_gone()



