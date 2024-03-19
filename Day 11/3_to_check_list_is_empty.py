# 3.Write a Python program to check if a list is empty.

rnge=int(input("Enter the how much range do you want in a list: "))
lst=[]
for i in range(rnge):
    variable_name=chr(97+i)
    value=int(input(f"Enter a number to store in a list {variable_name}: "))
    lst.append(value)
    
if len(lst)<=0:
    print("List is empty and the value is: ",lst)
else:
    print(f"List is not empty and the value is: {lst}")