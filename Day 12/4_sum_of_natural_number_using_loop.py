# 4. Write a Python program to find the sum of natural numbers up to \(n\) using a loop.

user=int(input("Enter the range of natural natural: "))

sum=0
for i in range(1,user+1):
    sum=sum+i

print(f"Sum of first {user} natural number is: {sum}")