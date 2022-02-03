# Given a hash, return a flat array containing all the hash’s keys and values.

input = {"a": 1, "b": 2, "c": 3, "d": 4}
# Output: [“a”, 1, “b”, 2, “c”, 3, “d”, 4]


def flatten_hash(input_hash):
    array = []
    for key, value in input_hash.items():
        array.append(key)
        array.append(value)
    return array


print(flatten_hash(input))
