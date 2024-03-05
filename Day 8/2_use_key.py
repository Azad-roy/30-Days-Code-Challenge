# Attempting to use a list as a key
try:
    # Creating a dictionary with a list as a key
    dict_with_list_key = {
        [1, 2]: "value",
        }
    print("This line will not be reached due to TypeError")
except TypeError as e:
    print("TypeError:", e)

# Using a tuple as a key
# Creating a dictionary with a tuple as a key
dict_with_tuple_key = {
    (1, 2): "value",
    }

# Accessing the value using the tuple key
print("Value associated with key (1, 2):", dict_with_tuple_key[(1, 2)])

# Attempting to use a list as a key
# Creating a dictionary with a list as a key
# This will raise a TypeError
# dict_with_list_key = {[1, 2]: "value"}

# Using a tuple as a key
# Creating a dictionary with a tuple as a key
# dict_with_tuple_key = {[1, 2]: "value"}

# # Accessing the value using the tuple key
# print("Value associated with key (1, 2):", dict_with_tuple_key[(1, 2)])