# Write a function that returns the greatest value from an array of numbers.

# Input: [5, 17, -4, 20, 12]
# Output: 20

def greatest_num(nums):
    count = 0
    for num in nums:
        if num > count:
            count = num
    return count


print(greatest_num([5, 17, -4, 20, 12])) # => 20
