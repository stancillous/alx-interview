#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each
denomination of coin in the list
Your solution’s runtime will be evaluated in this task

"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    count = 0
    lg_idx = 0
    coins.sort(reverse=True)

    while total > 0 and lg_idx < len(coins):
        largest = coins[lg_idx]
        count += total // largest
        total %= largest
        lg_idx += 1
    if total != 0:
        return -1
    return count
