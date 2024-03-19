# 5. Write a Python program to display the multiplication table of a given integer.

user=int(input("Enter a number: "))

# mul=1
for i in range(1,11):
    mul=user*i
    print(f"{user}X{i}={user*i}")

print(f"Multiplication Table of {user} is: {mul}")