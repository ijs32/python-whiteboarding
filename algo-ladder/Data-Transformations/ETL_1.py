# You are given two parameters, an array and a number. Return a hash whose keys are each of the values from the array parameter, and whose values are the number parameter.

# Input:

arr = ["a", "e", "i", "o", "u"]
num = 1

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }


def etl_one(arr, num):
    answer = {}
    for char in arr:
        answer[char] = num
    return answer


print(etl_one(arr, num))
