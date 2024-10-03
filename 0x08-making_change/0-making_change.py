#!/usr/bin/python3
"""
Main file for testing

"""


def makeChange(coins, total):
    """Sort coins in descending order for optimization"""
    if total <= 0:
        return 0
    # Sort coins in descending order for optimization
    coins.sort(reverse=True)
    # Initialize cache
    cache = {}

    def dfs(remaining):
        # Base cases
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        # Check cache
        if remaining in cache:
            return cache[remaining]
        # Try each coin
        min_coins = float('inf')
        for coin in coins:
            if coin > remaining:
                continue
            num_coins = dfs(remaining - coin)
            if num_coins != float('inf'):
                min_coins = min(min_coins, num_coins + 1)

        # Cache the result
        cache[remaining] = min_coins
        return min_coins
    result = dfs(total)
    return result if result != float('inf') else -1
