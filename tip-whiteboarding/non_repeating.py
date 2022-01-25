# first non repeating character

# O(2n)
def non_repeating(word):
    chars = {}
    i = 0
    for char in word:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for key, value in chars.items():
        if value == 1:
            return key


print(non_repeating("leet")) # => l
print(non_repeating("racecar")) # => e
