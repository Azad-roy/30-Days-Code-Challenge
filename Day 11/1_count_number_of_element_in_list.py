# 1.Write a Python program to count the number of elements in a list.

rnge=int(input("Enter the how much range do you want in a list: "))
lst=[]
for i in range(rnge):
    variable_name=chr(97+i)
    value=int(input(f"Enter a number to store in a list {variable_name}: "))
    lst.append(value)
    
# print(lst)
print(f"Total element in list is: {len(lst)}")