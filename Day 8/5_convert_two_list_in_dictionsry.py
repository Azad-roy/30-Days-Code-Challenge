# # 5.Convert two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], into a dictionary.

keys=['a', 'b', 'c']
values=[1, 2, 3]

for i in range(len(keys)):
    
    my_dict={
        keys[i]:values[i],
    }
    print(my_dict)