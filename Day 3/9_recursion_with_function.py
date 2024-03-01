# 9.Use recursion to calculate the factorial of a number.

def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
    
user=int(input("Enter a number to find the factorial: "))
print(f"Factorial of {user} is: {factorial(user)}")