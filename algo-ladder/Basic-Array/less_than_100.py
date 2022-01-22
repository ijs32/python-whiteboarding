# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]

def less_than_100(nums):
    list = []
    for num in nums:
        if num < 100:
            list.append(num)
    return list


print(less_than_100([99, 101, 88, 4, 2000, 50]))  # => [99, 88, 4, 50]
