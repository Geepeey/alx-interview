#!/usr/bin/python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """Result in exactly n H characters in the file"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    return operations
