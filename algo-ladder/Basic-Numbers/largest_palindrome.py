# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = 0
i = 900
while i < 1000:
    i2 = 900
    while i2 < 1000:
        reversed_list = list(reversed(str(i * i2)))
        reverse = ""
        reverse = int(reverse.join(reversed_list))
        if (i * i2 == reverse) and (i * i2 > palindrome):
            palindrome = i * i2
        i2 += 1
    i += 1

print(palindrome)
