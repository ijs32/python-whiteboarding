# Given two sorted arrays, merge the second array into the first array while ensuring that the first array remains sorted. Do not use any built-in sort methods.

# Input :
# A : [1, 5, 8]
# B : [6, 9]

# Modified A : [1, 5, 6, 8, 9]


def merge_arr(arr1, arr2):
    merged = []
    for num1 in arr2:
        for i, num2 in enumerate(arr1):
            if num1 > num2 and num1 <= arr1[i + 1]:
                merged.append(num1)
            else:
                merged.append(num2)
    return merged


print(merge_arr([1, 5, 8], [6, 9]))
