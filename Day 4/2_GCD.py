# 2.Write a program to find the GCD (Greatest Common Divisor) of two numbers.

def GCD(x,y):
    if y==0:
        return x
    else:
        return GCD(y,x%y)
    
n1,n2=[int(n1) for n1 in input("Enter two numbers separated: ").split()]
print(f"The GCD of {n1} and {n2} is: {GCD(n1,n2)}")