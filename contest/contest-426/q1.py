"""
You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits.

A set bit refers to a bit in the binary representation of a number that has a value of 1.


"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            if all (x == '1' for x in bin(n)[2:]):
                return n


