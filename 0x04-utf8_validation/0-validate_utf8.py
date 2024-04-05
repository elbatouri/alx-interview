#!/usr/bin/python3
"""
UTF-8 Validation

This module contains a function that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.

    A character in UTF-8 can be 1 to 4 bytes long. The data set can
    contain multiple characters. The data will be represented by a
    list of integers, where each integer represents 1 byte of data,
    therefore you only need to handle the 8 least significant bits
    of each integer.
    """
    number_bytes = 0
    mask_1 = 1 << 7

    for i in range(0, len(data), 1):

        if number_bytes == 0:

            # Calculate the number of leading 1 bits in the first byte
            num_leading_ones = bin(data[i]).count('1')

            if num_leading_ones == 0:
                continue

            if num_leading_ones > 4:
                return False

            number_bytes = num_leading_ones - 1

        else:
            # Check if the current byte starts with 10
            if not (data[i] & mask_1 and not (data[i] & (mask_1 >> 1))):
                return False

        number_bytes -= 1

    # Check if any of the bytes is not a continuation byte
    if any(not (b & mask_1 and not (b & (mask_1 >> 1)))
           for b in data if b & mask_1):
        return False

    return True
