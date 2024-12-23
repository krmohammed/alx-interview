#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """makeChange function

    Args:
        coins (list): values of coins
        total (int): given amount
    """
    if total <= 0:
        return 0
    tot = total
    coins.sort()
    l = len(coins) - 1
    ret = []
    while l >= 0:
        while tot >= coins[l]:
            tot -= coins[l]
            ret.append(coins[l])
        l -= 1
    if total != sum(ret):
        return -1
    return len(ret)
