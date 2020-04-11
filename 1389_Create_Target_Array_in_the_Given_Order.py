# Input: nums = [0,1,2,3,4] index = [0,1,2,2,1]   Output: [0, 4, 1, 3, 2]
# The object of this program is to make a new list that takes the elements from "nums" and puts them at the index of "index"

# This is the elements we want to get. 
nums = [0,1,2,3,4]
# This is the index we want to place in the element. 
index = [0,1,2,2,1]
# This is the target list.
target_list = []
# n is the number, i is the index. 
# Zip allows us to itereate over two lists at the same time . 
for n,i in zip(nums,index):
    # Insert places the number at the index. 
  target_list.insert(i,n)
print(target_list)
