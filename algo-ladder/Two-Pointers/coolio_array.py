# Given an array of numbers, return true if the array is a "100 Coolio Array", or false if it is not.

# A "100 Coolio Array" meets the following criteria:

# Its first and last numbers add up to 100,
# Its second and second-to-last numbers add up to 100,
# Its third and third-to-last numbers add up to 100,
# and so on and so forth.

# Here are examples of 100 Coolio Arrays:

# [1, 2, 3, 97, 98, 99]
# [90, 20, 70, 100, 30, 80, 10]

def coolio(arr):
    count = 0
    for i, num in enumerate(arr):
        if num + arr[-i - 1] == 100:
            count += 1
        elif (num == arr[-i - 1]) and num == 100:
            count += 1
    return count == len(arr)


print(coolio([1, 2, 3, 97, 98, 99]))  # => True
print(coolio([90, 20, 70, 100, 30, 80, 10]))  # => True
print(coolio([90, 20, 70, 10, 30, 80, 10]))  # => False
