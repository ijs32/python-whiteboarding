# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

string = "abcdefghhijkkloooop"


def first_dup(string):
  for i in range(len(string)):
    for i2 in range(len(string)):
      if (i != i2) and (string[i] == string[i2]):   # non linear solution, will be back with
        return string[i]                           # linear one soon


print(first_dup(string)) # => "h"