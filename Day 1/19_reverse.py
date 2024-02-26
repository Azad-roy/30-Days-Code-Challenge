def reverse(str):
    for i in range(len(str),0,-1):
        print(str[i-1],end="")
        
str=input("Enter any word or sentence: ")
reverse(str)