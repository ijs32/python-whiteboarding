# Given two arrays, determine whether one is a subset of the other. It is considered a subset if all the values in one array are contained within the other.

# note: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 2]
# Output: true

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 7]
# Output: false

# is a subset
# O(2n)
def is_subset(big_arr, small_arr):
    hash = {}
    for num in big_arr:
        hash[num] = num # add all big_arr values to a hash

    for num in small_arr:
        if not num in hash:
            return False  # go through all the values and break if one isnt present
    return True  # if all values are present return True


big_arr = [1, 2, 3, 4, 5, 6]
print(is_subset(big_arr, [6, 3, 2]))  # => True
print(is_subset(big_arr, [6, 3, 7]))  # => False
