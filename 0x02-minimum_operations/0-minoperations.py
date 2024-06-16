#!/usr/bin/env python3
"""Minimum Operation"""


def minOperations(n: int) -> int:
    """Get the minimum operations in a file"""
    if n <= 0:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
