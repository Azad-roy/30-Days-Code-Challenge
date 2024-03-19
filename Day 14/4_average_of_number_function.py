def avera(rang):
    adds=0
    for j in range(0,len(rang)):
        adds=adds+rang[j]
        
    avg=adds/len(rang)
    return avg

ran=int(input("Enter the range of list: "))
lst=[]
for i in range(ran):
    user=int (input(f"Enter number in position {i+1}: "))
    lst.append(user)
    
print(f"Average of {lst} is: {avera(lst)}")