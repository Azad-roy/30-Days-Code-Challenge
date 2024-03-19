# 1. Write a Python function that takes two numbers as arguments and returns their sum.
def sum(x,y):
    return x+y
    
a,b=[int(a) for a in (input("Please enter two number in saperate: ")).split()]
print(f"Sum is: {sum(a,b)}")