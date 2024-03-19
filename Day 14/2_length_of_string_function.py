# 2. Write a Python function that takes a string as input and returns the length of the string.

def length(stri):
    store=len(stri)
    return f"Length of the string: is {len(stri)}"

user=input("Please enter any string: ")
print(length(user))