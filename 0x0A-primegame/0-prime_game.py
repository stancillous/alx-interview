#!/usr/bin/python3

"""PRIME GAME
Determine who the winner of a game is
"""


def isPrime(num: int):
    """determines if a number is Prime"""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def replacePrimeAndDuplicates(num, nums):
    """function to remove/replace the prime number
    and its multiples from the set(list)"""
    for i in range(len(nums)):
        if nums[i] % num == 0:
            nums[i] = 1
    return nums


def isWinner(x, nums):
    """determine who the winner of a game is"""
    turn = "Maria"
    rounds = 0
    mariaWins = 0
    benWins = 0

    for num in nums:
        if rounds < x:
            new_nums = list(range(1, num+1))
            for i in new_nums:
                if isPrime(i):
                    new_nums = replacePrimeAndDuplicates(i, new_nums)
                    turn = "Maria" if turn == "Ben" else "Ben"
            if turn == "Maria":
                benWins += 1
            else:
                mariaWins += 1
            rounds += 1
            turn = "Maria"
    return "Maria" if mariaWins > benWins else "Ben"
