# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]
def mesh(arr_1):
    mesh = []
    for char1 in arr_1:
        for char2 in arr_1:
            if char1 != char2:
                mesh.append(char1 + char2)
    return mesh


print(mesh(["a", "b", "c", "d"])) # => ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]
