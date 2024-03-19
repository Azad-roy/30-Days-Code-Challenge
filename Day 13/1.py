# 1. Write a Python program that takes a list of numbers and separates them into positive, negative, and zero lists using list comprehensions.

positive=[]
negative=[]
zero=[]

lst=[1,21,-5,0,-45,5,-7]
for i in lst:
    if i==0:
        zero.append(i)
    elif i<0:
        negative.append(i)
    else:
        positive.append(i)
        
print(f"Psitive number of list is: {positive}")
print(f"Negative number of list is: {negative}")
print(f"Zero number of list is: {zero}")