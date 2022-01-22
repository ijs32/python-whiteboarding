# Write a function that prints out every number from 1 to N, with the following exceptions:

# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".

def fizzbuzz(num):
    for i in range(1, num):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FIZZBUZZ and number =", i)
        elif (i % 3 == 0):
            print("FIZZ and number =", i)
        elif (i % 5 == 0):
            print("BUZZ and number =", i)


fizzbuzz(100)
