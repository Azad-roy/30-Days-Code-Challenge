# 5.Write a Python program to sort a list of elements.

rnge=int(input("Enter the how much range do you want in a list: "))
lst=[]
for i in range(rnge):
    value=int(input(f"Enter a number to store in a list: "))
    lst.append(value)

lst.sort()
print("Please Wait! Sorting...")
print(f"Sorted list is: {lst}")