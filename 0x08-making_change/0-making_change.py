#!/usr/bin/python3
"""
a program
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins values.
    ARGS:
    coins: list of coin values
    total: an int of total target
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
            return -1
    else:
        return min_coins[total]
