# # 2.Create a program to print the first N prime numbers.

# def prime(num):
#     if num%

# user=int(input("Enter the range of prime numbers: "))
# prime(user)


def print_first_n_primes(n):
    count, num = 0, 2
    while count < n:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            print(num, end=" ")
            count += 1
        num += 1

if __name__ == "__main__":
    n = int(input("Enter the value of N: "))
    print("First", n, "prime numbers are:")
    print_first_n_primes(n)