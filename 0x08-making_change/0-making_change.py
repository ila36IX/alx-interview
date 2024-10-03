#!/usr/bin/python3
"""
Main file for testing

"""


def makeChange(coins, total):
    """If the total is 0 or less, return 0 (no coins needed)"""
    if total <= 0:
        return 0

    # Initialize dp array to a value larger than any possible number of coins
    # (e.g., total + 1)
    dp = [float('inf')] * (total + 1)

    # Base case: to make 0 amount, we need 0 coins
    dp[0] = 0

    # Loop through each coin in the list
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, we can't make the total with the given
    # coins
    return dp[total] if dp[total] != float('inf') else -1
