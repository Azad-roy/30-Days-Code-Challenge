# 2. Implement a Python program to determine whether a given year is a leap year or not using conditional statements. 

user=int(input("Enter a year: "))

if (user%100!=0) or (user%4==0 and user%400==0):
    print(f"{user} is a leap year")
else:
    print(f"{user} is not a leap year")