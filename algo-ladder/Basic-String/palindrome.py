# Given a string, write a function that returns true if it is a palindrome, and false if it is not. (A palindrome is a word that reads the same both forward and backward.)

# Input: “racecar”
# Output: true

# Input: “baloney”
# Output: false

def is_palindrome(string):
    reversed = ""
    i = len(string) - 1
    while i >= 0:
        reversed += string[i]
        i -= 1
    return reversed == string


print(is_palindrome(string="racecar"))  # => True
print(is_palindrome(string="baloney"))  # => False
