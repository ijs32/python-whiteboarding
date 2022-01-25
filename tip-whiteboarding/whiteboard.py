# Given two arrays, determine whether one is a subset of the other. It is considered a subset if all the values in one array are contained within the other.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 2]
# Output: true

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 7]
# Output: false

# is a subset
'''
def is_subset(big_array, small_array):
    hash = {}
    count = 0
    for num in big_array:
        hash[num] = 0
    for k in hash:
        if k == small_array[0]:
            count += 1
        if k == small_array[1]:
            count += 1
        if k == small_array[2]:
            count += 1
    print(count == len(small_array))


is_subset([1, 2, 3, 4, 5, 6], [6, 3, 2])
'''

# first non repeating character
'''
word = "leet"


def non_repeating(word):
    chars = {}
    i = 0
    while i < len(word):
        chars[word[i]] = True
        i += 1
    count = 0
    while i < len(word):
        chars[word[i]]
        i += 1
    return chars


print(non_repeating(word))
'''
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# 1 2 3
# 4 5 6
# 9 8 9
# absolute difference is 2.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [9, 8, 9]
# ]


# def difference_of_matrix(arr):
#     sum_1 = 0
#     sum_2 = 0
#     for i, arr1 in enumerate(arr):
#         sum_1 += arr1[i]
#         sum_2 += arr1[-1 + -i]
#     return abs(sum_1 - sum_2)


# print(difference_of_matrix(matrix))

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [4,1,2,1,2]
# Output: 4

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
