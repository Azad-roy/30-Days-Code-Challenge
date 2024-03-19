# 1.Check if the value 25 exists in the values of `my_dict`.

my_dict={
    "a":5,
    'b':24,
    '''c''':25,
}

if 25 in my_dict.values():
    print("yes! 25 value is exists in my_dict")      
else:
    print("No! 25 value is don't exists in my_dict")