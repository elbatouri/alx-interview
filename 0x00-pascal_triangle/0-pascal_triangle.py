#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified level n.

    Args:
    - n: The number of levels for Pascal's Triangle.

    Returns:
    - A list of lists representing Pascal's Triangle.
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = [1]  # The first element in every row is always 1
            for j in range(1, i):
                # Calculate the binomial coefficient
                value = row[j - 1] * (i - j) // j
                row.append(value)
            triangle.append(row)

    return triangle
