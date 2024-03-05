# 4.Remove the last inserted key-value pair from `my_dict`.

my_dict ={
    "name": "Alice",
    "age": "Sweet 18",
}

removed=my_dict.popitem()
print(f"Removed value are: {removed}")
print(f"Current values in dictionary is: {my_dict}")