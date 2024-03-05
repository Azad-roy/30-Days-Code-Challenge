# 2.Print all the values in `my_dict` using a loop.

my_dict={}
key_value={
    "name":"Alice"
}
my_dict.update(key_value)

key_value={
    "Bob":"Alice"
}
my_dict.update(key_value)

for values in my_dict.values():
    print(values)