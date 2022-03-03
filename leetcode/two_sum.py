nums = [2, 7, 11, 15]
target = 9


def two_sum(nums, target):
    checked = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in checked:
            return [checked[diff], i]
        else:
            checked[num] = i


print(two_sum(nums, target))
