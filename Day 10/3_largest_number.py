# 4. Write a Python program to get the largest number from a list.


def large(num):
    store=num[0]
    for i in num:
        if i>store:
            store=i
    return store
lst=[1, 2, 3, 4, 10,0,1]
print(f"Largest number is: {large(lst)}")