# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [4,1,2,1,2]
# Output: 4

# O(2n)
def only_one(arr):
    dict = {}
    for i, num in enumerate(arr):
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for key, value in dict.items():
        if value == 1:
            return key


print("The answer is :", only_one(arr=[4, 1, 2, 1, 2]))
