# 5.Use dictionary unpacking to create a new dictionary by combining `dict1` and `dict2`.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

combined_dict = {**dict1, **dict2}

print(combined_dict)