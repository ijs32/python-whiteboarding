# The Collatz Conjecture or 3x+1 problem can be summarized as follows:

# Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

# Given a number n, return the number of steps required to reach 1.

# Examples
# Starting with n = 12, the steps would be as follows:

# 12
# 6
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1

# Resulting in 9 steps. So for input n = 12, the return value would be 9.
num = int(input("Please enter a number : "))


def collatz_conjecture(num):
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
            steps += 1
            print("On step #{} your number is equal to: {}".format(steps, num))
        else:
            num = num * 3 + 1
            steps += 1
            print("On step #{} your number is equal to: {}".format(steps, num))
    return steps


print("the number {} took {} steps to get to 1".format(
    num, collatz_conjecture(num)))
# => The number 12 took 9 steps to get to 1
# example input 129001 took 193 steps to get to 1
