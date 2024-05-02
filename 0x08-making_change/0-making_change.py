#!/usr/bin/python3

def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    
    # Initialize the dynamic programming array
    dp = [0] + [float('inf')] * total
    
    # Iterate through each coin denomination
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Check if the total can be achieved
    return dp[total] if dp[total] != float('inf') else -1
