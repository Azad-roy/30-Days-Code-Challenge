def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b

x,y=[int(x) for x in input("Enter two numbers: ").split()]
print(f"Add of {x} and {y} is {sum(x,y)}")
print(f"Sub of {x} and {y} is {sub(x,y)}")
print(f"Divide of {x} and {y} is {div(x,y)}")
print(f"multiply of {x} and {y} is {mul(x,y)}")