# 3.Implement a function to check if a given string has all unique characters.

def check_unique(char):
    store=set()
    for i in char:
        if i in store:
            return False
        store.add(i)
    return True

user=input("Enter any word or sentence: ")
print(f"'{user}' has all unique characters: {check_unique(user)}")