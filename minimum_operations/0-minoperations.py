#!/usr/bin/python3
"""Calculates the fewest operations to reach n H characters."""


def minOperations(n):
    """Return the minimum Copy All/Paste operations to get n H's, or 0."""
    if type(n) is not int:  # not a whole number
        return 0
    if n < 2:  # 1 needs no operations, 0 and negatives are impossible
        return 0

    operations = 0
    remaining = n

    # 2 is the only even prime, so handle it on its own
    while remaining % 2 == 0:
        operations = operations + 2
        remaining = remaining // 2

    # every other prime is odd, so only try odd divisors
    divisor = 3
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            operations = operations + divisor
            remaining = remaining // divisor
        divisor = divisor + 2

    # anything left over is a single prime factor bigger than its square root
    if remaining > 1:
        operations = operations + remaining

    return operations