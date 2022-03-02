def contains_duplicate(nums):
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 0
    for key, value in nums_dict.items():
        if value > 0:
            return True
    return False


print(contains_duplicate([1, 2, 3, 0]))
