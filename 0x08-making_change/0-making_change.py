#!/usr/bin/python3
"""Making Change Module.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the dp array to find the minimum number
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), the total cannot
    if dp[total] == float('inf'):
        return -1

    return dp[total]
