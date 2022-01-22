# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

def double_values(nums):
    return nums * 2


print(list(map(double_values, [4, 2, 5, 99, -4]))) #=> [8, 4, 10, 198, -8]
