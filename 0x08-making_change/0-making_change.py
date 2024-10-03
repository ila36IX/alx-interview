#!/usr/bin/python3
"""
Main file for testing
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, it means we couldn't make the amount
    return dp[total] if dp[total] != float('inf') else -1
