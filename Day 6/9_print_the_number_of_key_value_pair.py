# 9.Print the number of key-value pairs in `my_dict`.

def count(dicti):
    store=len(dicti)
    print(f"{store} times")

my_dict={}
key_value={
    "name":"Alice"
}
my_dict.update(key_value)

key_value={
    "Bob":"Alice"
}
my_dict.update(key_value)
count(my_dict)