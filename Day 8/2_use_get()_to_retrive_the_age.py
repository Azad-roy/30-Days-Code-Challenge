# 2.Use the `get()` method to retrieve the value for the key 'age' from `my_dict`, with a default value of 0.

my_dict={
    "name":"Alice",
    'City':'Alaska',
}

retrieving=my_dict.get("age",0)
print("Age is:",retrieving)