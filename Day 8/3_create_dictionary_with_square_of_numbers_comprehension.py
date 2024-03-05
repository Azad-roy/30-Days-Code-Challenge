# 3.Create a dictionary with squares of numbers from 1 to 5 using dictionary comprehension.

square_dict={}

for i in range(1,6):
    square_dict={i:i**2}
    print(square_dict)