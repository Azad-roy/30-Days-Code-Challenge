# 6.Write a program that takes a list of numbers and returns the sum of even numbers.

user=int(input("Enter the range of list: "))
my_list=[]

for i in range(0,user):
    l1=int(input(f"Enter the value in list position {i+1}: "))
    my_list.append(l1)

add=0

for j in range(len(my_list)):
    if my_list[j]%2==0:
        add=add+my_list[j]

print(my_list)
print(f"Sum of even number in list {my_list} is: {add}")