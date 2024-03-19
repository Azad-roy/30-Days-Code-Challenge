# 3. Write a Python program to find the factorial of a number using a loop.

user=int(input("Enter a number: "))

store=1
for i in range(user,0,-1):
    store=store*i
    
print(store)