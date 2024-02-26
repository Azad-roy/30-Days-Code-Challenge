# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
list2=[]
list3=[]
# Use list comprehension to create a new list with squared elements
for i in numbers:
     list2.append(i**2)
     list3.append([i**2])
print(list2)
print(list3)
