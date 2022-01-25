# #1
# Write a function that accepts an array of numbers, and returns an array of the products of every pair of numbers from the array.

# Example:
# Input: [3, 4, 5, 6]
# Output: [12, 15, 18, 20, 24, 30]

li = [3, 4, 5, 6]


def products(li):
    products = []
    for i, num1 in enumerate(li):
        for i2, num2 in enumerate(li):
            if not (num1 * num2) in products and (i != i2):
                products.append(num1 * num2)
    return products


print(products(li))  # => [12, 15, 18, 20, 24, 30]
