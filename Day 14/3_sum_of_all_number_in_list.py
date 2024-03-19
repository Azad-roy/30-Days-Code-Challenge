# 3. Write a Python function that takes a list of numbers as input and returns the sum of all the numbers in the list.

def sums(rang):
    adds=0
    for j in range(0,len(rang)):
        adds=adds+rang[j]
    return adds

ran=int(input("Enter the range of list: "))
lst=[]
for i in range(ran):
    user=int (input(f"Enter number in position {i+1}: "))
    lst.append(user)

# print(lst)
print(f"Sum of {lst} is: {sums(lst)}")