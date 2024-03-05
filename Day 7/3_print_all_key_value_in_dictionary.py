# 3.Print all key-value pairs in `my_dict` using a loop.

my_dict={}
key_value={
    "name":"Alice"
}
my_dict.update(key_value)

key_value={
    "Bob":"Alice"
}
my_dict.update(key_value)

for i in range (1,len(my_dict)):
    print(my_dict)