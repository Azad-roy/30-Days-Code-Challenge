# 10.Remove the key-value pair with the key 'name' from `my_dict`.

my_dict={}
key_value={
    "name":"Alice"
}
my_dict.update(key_value)

key_value={
    "Bob":"Alice"
}
my_dict.update(key_value)
del my_dict["name"]
print(my_dict)