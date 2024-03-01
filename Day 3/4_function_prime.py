# 4.Implement a function to check if a number is a prime number.

def prime_number(num):
    if(num==2 or num==3):
        print(f"This is a prime number")
    elif num%2!=1 and num%2==0:
        print("This is not a prime number")
    elif(num%3!=1 and num%3==0):
        print("This is not a prime number")
    elif(num%5==0):
        print("This is not a prime number")
    else:
        print("This is a prime number")
        

user=(int(input("Enter a number: ")))
prime_number(user)