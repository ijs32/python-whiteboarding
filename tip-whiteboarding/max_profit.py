# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
prices = [7, 1, 5, 3, 6, 4]  # => 5


def max_profit(prices):
    profit = 0
    for i1, num1 in enumerate(prices):
        for i2, num2 in enumerate(prices):
            if i2 > i1 and num2 - num1 > profit:
                profit = num2 - num1
    return profit


print(max_profit(prices))  # => 5

# def max_profit(prices):
#     numbers = {}
#     profit = 0
#     min = 0
#     max = 0
#     for i, num in enumerate(prices):
#         numbers[num] = i
#     for key, value in numbers.items():        # unfinished attempt
#         if key > max and max - min > profit:
#           max = key
#     return numbers


# print(max_profit(prices))
