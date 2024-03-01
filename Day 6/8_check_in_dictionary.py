# 8.Check if the key 'age' exists in `my_dict`.

def check(dict):
    if "age" in dict:
        return True
    else:
        return False    
my_dict={}
key_value={
    "name":"Alice",
}
key_value={
    "Bob":"Alice",
}

my_dict.update(key_value)
print(check(my_dict))