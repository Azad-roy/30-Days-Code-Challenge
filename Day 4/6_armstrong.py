# 4.Write a function to check if a number is an Armstrong number.

def armstrong(num):
    sum=0
    copy=num
    order=len(str(num))
    while(num>0):
        digit=num%10
        print(digit)
        sum+=digit**order
        num=num//10
    if sum==copy:
        print(f"{copy} is an Armstrong number")
    else:
        print(f"{copy} is not an Armstrong number")

user=int(input("Enter a number: "))
armstrong(user)