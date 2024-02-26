# # palindrome=input("Enter any word or sentence: ")
# # for i in range(0,len(palindrome)):
# #     if(palindrome[i]==palindrome[len(palindrome)-1]):
# #         print("Yes")

# def is_palindrome(s):
#     # Remove spaces and convert to lowercase
#     s = s.replace(" ", "").lower()
    
#     # Compare the original string with its reverse
#     return s == s[::-1]

# # Test the function
# string_to_check = input("Enter a string: ")
# if is_palindrome(string_to_check):
#     print("Yes, it's a palindrome!")
# else:
#     print("No, it's not a palindrome.")

palindrome =input("Enter any word or sentence: ")
for i in range(len(palindrome),0,-1):
    # a=print(palindrome[i-1],end="")
    a=palindrome[i-1]
    
for i in range(len(palindrome),0,-1):
    print(a[i-1],end="")
# print(type(a))
# if palindrome in a:
#     print("this is a palindrome")
# else:
#     print("This is not palindrome")
























