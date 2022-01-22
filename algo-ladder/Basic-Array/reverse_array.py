# Given an array, write a function that returns an array that contains the original array’s values in reverse.

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def reverse_array(nums):
    reverse = []
    i = len(nums) - 1
    while i >= 0:
        reverse.append(nums[i])
        i -= 1
    return reverse


print(reverse_array([1, 2, 3, 4, 5])) #=> [5, 4, 3, 2, 1]
