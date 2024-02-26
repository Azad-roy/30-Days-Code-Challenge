def maximum(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greater number")
    elif(b>c):
        print(f"{b} is greater number")
    else:
        print(f"{c} is greater number")
    
x,y,z=[int(x) for x in(input("Enter three any numbers: ")).split()]
maximum(x,y,z)