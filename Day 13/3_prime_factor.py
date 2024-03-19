# 3. Create a Python program that prints the prime factors of a given number using a loop.

def prime_factors(num):
    factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            print(divisor)
            factors.append(divisor)
            num //= divisor
        divisor += 1

    return factors
try:
    num = int(input("Enter a number to find its prime factors: "))
    if num <= 0:
        raise ValueError("Please enter a positive integer.")
        
    print(f"Prime factors of {num}: {prime_factors(num)}")
    
except ValueError as ve:
    print(ve)