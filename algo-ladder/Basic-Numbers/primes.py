# Write a function that returns whether a given number is a prime number.

def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True


print(is_prime(5))  # => True
print(is_prime(129))  # => False
