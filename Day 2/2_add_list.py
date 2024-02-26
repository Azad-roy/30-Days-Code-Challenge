# 2.Add two lists element-wise and print the result.

list1=[4,5,6,1]
list2=[7,8,5,2]
result=[]

for i in range(len(list1)):
    result.append(list1[i]+list2[i])
    
print(f"Sum of two list is: {result}")