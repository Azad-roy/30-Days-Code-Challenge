# 1. Write a Python program that checks if a number is positive, negative, or zero.

user=int(input("Enter a number: "))

if user>0:
    print(f"{user} is a positive number")
elif(user<0):
    print(f"{user} is a negative number")
else:
    print(f"{user} is nor positive and nither negative")