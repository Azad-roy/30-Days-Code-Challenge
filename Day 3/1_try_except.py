# 1.Use a try-except block to handle division by zero in a program.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result of the division is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as error:
    print(f"Here print the error message: {error}")