# 2.Implement a function to calculate the Fibonacci sequence.

def fibonacci(self):
    if self<=1:
        return self
    else:
        return fibonacci(self-1)+fibonacci(self-2)

user=(int(input("Enter a number: ")))
print(fibonacci(user))
if user<0:
    print("Please enter positive number")
else:
    for i in range(user):
        print(fibonacci(i))