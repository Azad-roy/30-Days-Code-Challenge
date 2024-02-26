def factorial(fact):
    if(fact==1):
        return 1
    elif(fact==0):
        return 1
    return fact*factorial(fact-1)

num=int(input("Enter a number to calculte the factorial: "))
print(f"Factorial of {num} is: ",factorial(num))