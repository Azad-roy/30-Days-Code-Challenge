# 5.Create a function to find the LCM (Least Common Multiple) of two numbers.

def LCM(num1,num2):
    if num1>num2:
        higher=num1
    else:
        higher=num2

    value=higher

    while True:
        if higher%num1==0 and higher%num2==0:
            return (f"LCM of {num1} and {num2} is: {higher}")
        higher=higher+value
    
num1,num2=[int(num1) for num1 in (input("Enter two numbers: ")).split()]
print(LCM(num1,num2))