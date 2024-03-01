# 2.Create a function to calculate the power of a number.

def calculate_power(number, pow):
    return f"{pow} is a power of {number} and result is: {number**pow}"

num=int(input("Enter a number: "))
power=int(input("Enter a Number to set power of a number: "))

print(calculate_power(num, power))