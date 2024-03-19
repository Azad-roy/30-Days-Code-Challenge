# 4.Write a Python program to reverse a list.

rnge=int(input("Enter the how much range do you want in a list: "))
lst=[]
for i in range(rnge):
    value=int(input(f"Enter a number to store in a list: "))
    lst.append(value)
    
lst.reverse()
print(f"Reverse number is: {lst}")