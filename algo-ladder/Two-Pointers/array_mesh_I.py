# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# Input: ["a", "b", "c"], ["d", "e", "f", "g"]
# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]
def mesh(arr_1, arr_2):
    mesh = []
    for char1 in arr_1:
        for char2 in arr_2:
            mesh.append(char1 + char2)
    return mesh


# => ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]
print(mesh(["a", "b", "c"], ["d", "e", "f", "g"]))
