# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: “silent”, “listen”
# Output: true

# Input: “frog”, “bear”
# Output: false

def anagrams(word1, word2):
    hash = {}
    for char in word1:
        hash[char] = char
    for char in word2:
        if not char in hash:
            return False
    return True


print(anagrams("silent", "listen"))  # => True
print(anagrams("frog", "bear"))  # => False
