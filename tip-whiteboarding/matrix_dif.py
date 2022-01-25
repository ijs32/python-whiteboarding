# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# 1 2 3
# 4 5 6
# 9 8 9
# absolute difference is 2.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]


def difference_of_matrix(arr):
    sum_1 = 0
    sum_2 = 0
    for i, arr1 in enumerate(arr):
        sum_1 += arr1[i]
        sum_2 += arr1[-1 + -i]
    return abs(sum_1 - sum_2)


print(difference_of_matrix(matrix))