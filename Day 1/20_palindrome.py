def reverse(str):
    a=""
    for i in range(len(str),0,-1):
        a=a+str[i-1]
    return a
str=input("Enter any word or sentence: ")
if reverse(str) in str:
    # print(reverse(str))
    print(f"{str}; is palindrome")
else:
    print(f"{str}; is not palindrome")