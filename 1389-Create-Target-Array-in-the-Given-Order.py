nums = [0,1,2,3,4]
index = [0,1,2,2,1]
t_list = []
for n,i in zip(nums,index):
  t_list.insert(i,n)
print(t_list)
