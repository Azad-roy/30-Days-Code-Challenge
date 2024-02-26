# 5.Convert a list to a set and then back to a list.

my_list=[1,2,3,4]
print(type(my_list))

my_list=set(my_list)
print(type(my_list))

my_list=list(my_list)
print(type(my_list))