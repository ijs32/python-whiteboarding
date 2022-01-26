# Find the largest product of any two numbers within a given array.

# Input: [5, -2, 1, -9, -7, 2, 6]
# Output: 63 (-9 * -7)

def largest(arr):
    product = 0
    for num1 in arr:
        for num2 in arr:
            if num1 * num2 > product and num1 != num2:
                product = num1 * num2
    return product


print(largest([5, -2, 1, -9, -7, 2, 6]))
