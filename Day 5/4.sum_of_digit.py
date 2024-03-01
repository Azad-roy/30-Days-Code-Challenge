# 4.Create a function to calculate the sum of digits in a number.

def sum_digit(num):
    sum=0
    while(num>0):
        store=num%10
        sum=sum+store
        num=num//10
    return sum
user=int(input("Enter a number: "))
print(sum_digit(user))
