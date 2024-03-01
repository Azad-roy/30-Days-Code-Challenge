# 6.Write a program that takes a list of numbers and returns the sum of even numbers with function.
#Ye function ke help se bnaya hu aa h or dushra wla without function se bnaya hu aa h,Yha function ke help se hmlog list me values add kr rhe h,jo maine khud se smjh kr bnaya h.

def list1(num):
    my_list=[]
    for i in range(0,num):
        l1=int(input(f"Enter the number in list {i+1}: "))
        my_list.append(l1)
    return my_list
    
user=int(input("Enter the range of list: "))

count=list1(user)
add=0
for j in range(len(count)):
    if count[j]%2==0:
        add=add+count[j]
print(count)
print(add)