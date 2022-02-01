string = "Fly me to the moon   "


def last_word(string):
    string = string.rstrip()
    arr = string.split(" ")
    return len(arr[-1])


print(last_word(string))
