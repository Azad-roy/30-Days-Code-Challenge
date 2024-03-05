# 1.Print all the keys in `my_dict` using a loop.

my_dict={}
key_value={
    "name":"Alice"
}
my_dict.update(key_value)

key_value={
    "Bob":"Alice"
}
my_dict.update(key_value)
for i in my_dict.keys():
    print(i)
