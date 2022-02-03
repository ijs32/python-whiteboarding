# Given a hash, create a new hash that has the keys and values switched.

input = {"a": 1, "b": 2, "c": 3}
# Output: {1 => "a", 2 => "b", 3 => "c"}


def flip_hash(input_hash):
    flipped = {}
    for key, value in input_hash.items():
        flipped[value] = key
    return flipped


print(flip_hash(input))
