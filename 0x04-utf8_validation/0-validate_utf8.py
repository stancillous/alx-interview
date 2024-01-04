#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only
need to handle the 8 least significant bits of each integer

"""


# def validUTF8(data):
#     """checks if the data represents a
#     valid utf-i encoding"""
#     for num in data:
#         if num > 127:
#             return False
#     return True

def validUTF8(data):
    """checks if the data represents a
    valid utf-i encoding"""
    i = 0
    while i < len(data):
        byte = data[i]

        if byte < 128:
            # is an ASCII character
            i = i + 1

        else:
            # is a multibyte character
            number_bytes = determineNumberOfBytes(byte)
            if number_bytes == 0 or i + number_bytes > len(data):
                return False
            for j in range(1, number_bytes):
                if (data[i + j] & 0b11000000) != 0b10000000:
                    return False
            i = i + number_bytes
    return True


def determineNumberOfBytes(leadingByte):
    """Determines the number of bytes based on the
    high-order bits of the leading byte"""
    if (leadingByte & 0b10000000) == 0:
        return 1
    elif (leadingByte & 0b11100000) == 0b11000000:
        return 2
    elif (leadingByte & 0b11110000) == 0b11100000:
        return 3
    elif (leadingByte & 0b11111000) == 0b11110000:
        return 4
    else:
        return 0  # Invalid leading byte
