# Given an array of numbers, write a function that returns a new array in which only select numbers from the original array are included, based on the following details:

# The new array should always start with the first number from the original array. The next number that should be included depends on what the first number is. The first number dictates how many spaces to the right the computer should move to pick the next number. For example, if the first number is 2, then the next number that the computer should select would be two spaces to the right. This number gets added to the new array. If this next number happens to be a 4, then the next number after that is the one four spaces to the right. And so on and so forth until the end of the array is reached.

# Input:
# [2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]

# Output:
# [2, 3, 1, 2, 2, 1, 5, 2, 2]

from operator import index


def skip_it(nums):
    i = nums[0]         # the variable i will keep track of our skip lengths
    index_of_array = 0  # the variable index_of_array keeps track of where we are
    output = [nums[0]]  # output is of course our final solution
    while i >= 0:
        # this prevents the loop from continuing if
        if index_of_array > len(nums):
            break                       # our index gets bigger than the array length
        elif i > 0:
            index_of_array += 1
            i -= 1
        elif i == 0:
            output.append(nums[index_of_array])
            i = nums[index_of_array]    # gives us new length to skip by
    return output


# => [2, 3, 1, 2, 2, 1, 5, 2, 2]
print(skip_it([2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]))
