# 3.Write a program to print the Fibonacci sequence up to a certain number.

def fibonacci(self):
    if(self<=1):
        return self
    # elif(self==1):
    #     return 1
    else:
        return fibonacci(self-1)+fibonacci(self-2)
    
user=int(input("Enter a number: "))
if(user<0):
    print("Please enter a positive number")
else:
    for i in range(user):
        print(fibonacci(i))