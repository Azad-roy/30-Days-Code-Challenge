# 4.Check if the keys in `dict1` are the same as the keys in `dict2`.

dict1={
    "a":1,
    "b":2,
    'c':3,
    "d":4,
}

dict2={
    "b":6,
    "a":5,
    "d":8,
    'c':7,
}

for key in dict1:
    if key in dict2:
        print("The keys in dict1 are the same as the keys in dict2.")
    else:
        print("The keys in dict1 are not the same as the keys in dict2.")