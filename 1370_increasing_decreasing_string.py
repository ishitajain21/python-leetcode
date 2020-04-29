# Input: "aaabbbccc" Output: "abccbaabccba"
# Algorithm:
    # Pick the smallest character from s and append it to the result.
    # Pick the smallest character from s which is greater than the last appended character to the result and append it.
    # Repeat step 2 until you cannot pick more characters.
    # Pick the largest character from s and append it to the result.
    # Pick the largest character from s which is smaller than the last appended character to the result and append it.
    # Repeat step 5 until you cannot pick more characters.
    # Repeat the steps from 1 to 6 until you pick all characters from s.
    # In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.


# This function checks that all of the elements in inp are used in the output( This doesn't include the largest character reversal.)
def check_for_each_element_in_inp():
    # Checks that the input is empty( for error handling and that inp's elements are removed as they are put in the output.)
    if inp == "": print(out)
    else:
        # Calls these functions and then recursively calls itself. 
        pick_char_out()
        repeat_steps()
        check_for_each_element_in_inp()

def pick_char_out():
    # Global is used so that the variables can be toggled inside the function. 
    global out
    global out_for_check
    # The basic essence of the input is in start. No repeated letters. 
    start = ""
    # The for loop goes though everything in the input and puts the basic essence in the variable start. 
    for i in inp: 
        if i not in start: start += i
    # Appends the basic essence in the out_for_check
    out_for_check += start
    #Since the procedure asks for the letters in both front and back order, the [::-1] reverses it. 
    out += start + start[::-1]

def repeat_steps():
    global inp
    # As mentioned in the check_for function, the occurences in out_for_check are removed from inp. 
    for i in out_for_check: inp = inp.replace(i,"",1)

# The input:
inp = "aaabbbccc"
# This version doesn't have the largest to smallest letter step done so that we can check which letters have been used from inp.
out_for_check = ""
#This is the version that is printed out to the user. 
out = ""

check_for_each_element_in_inp()
