# 7.Write a program to find the common elements between two lists.


set_range1=int(input("Enter the range of list1: "))
list1=[]
for i in range(set_range1):
    set_value=int(input(f"Enter the value in list position {i+1}: "))
    list1.append(set_value)

set_range2=int(input("Enter the range of list2: "))
list2=[]
for j in range(set_range2):
    set_value2=int(input(f"Enter the value in list position {j+1}: "))
    list2.append(set_value2)
    
#converting in set to use the & operator:-
set1=set(list1)
set2=set(list2)
    
common=set1 & set2
# again converting in as usual(list)
commom_list=list(common)

print(commom_list)