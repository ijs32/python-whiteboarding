# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

def count_votes(arr):
    hash = {}
    for vote in arr:
        if not vote in hash:
            hash[vote] = 1
        else:
            hash[vote] += 1
    return hash


print(count_votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman",
      "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))  # => {"Dewey" => 6, "Truman" => 5}
