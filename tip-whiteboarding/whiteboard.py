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
