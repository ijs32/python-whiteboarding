# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: “popcorn is so cool isn’t it yeah i thought so”
# Output: “so thought i yeah it isn’t cool so is popcorn”

def reverse_words(string):
    list = string.split()
    reversed_list = []
    for i in range(-(len(list)), 0):
        reversed_list.append(list[i])
    return " ".join(reversed_list)


string = "popcorn is so cool isn’t it yeah i thought so"
# => "popcorn is so cool isn’t it yeah i thought so"
print(reverse_words(string))
