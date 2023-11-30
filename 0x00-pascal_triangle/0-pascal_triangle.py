#!/usr/bin/python3
"""function that returns a list of lists of integers
representing the pascal's triangle"""


def pascal_triangle(n):
    """
    function that returns a list of lists of integers
    representing the pascal's triangle
    """

    if n <= 0:
        return []

    final_list = []  # is an array of arrays
    topArray = [1]
    for i in range(n):
        final_list.append(topArray)
        lenTop = len(topArray)

        newArray = []
        newArray.append(1)  # first element

        for j in range(1, lenTop):
            num = topArray[j - 1] + topArray[j]
            newArray.append(num)
        newArray.append(1)  # last element
        topArray = newArray
    return final_list
