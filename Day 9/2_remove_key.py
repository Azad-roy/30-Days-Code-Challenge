# 3.Remove the key 'gender' from `my_dict` with a default value of 'Not specified'

my_dict = {
    'name': 'John', 
    'age': 30, 
    'gender': 'male',
}

removed=my_dict.pop("age")

print(f"Removed key is: {removed}")
print(f"Updated dictionary is: {my_dict}")