# #1
# Write a function that accepts an array of numbers, and returns an array of the products of every pair of numbers from the array.

# Example:
# Input: [3, 4, 5, 6]
# Output: [12, 15, 18, 20, 24, 30]

arr = [3, 4, 5, 6]

# O(n^2) need to fix, going to come back to it but struggling to think of an O(n) solution at the moment


def products(arr):
    products = []
    for i, num1 in enumerate(arr):
        for i2, num2 in enumerate(arr):
            if not (num1 * num2) in products and (num1 != num2):
                products.append(num1 * num2)
    return products


print(products(arr))  # => [12, 15, 18, 20, 24, 30]
