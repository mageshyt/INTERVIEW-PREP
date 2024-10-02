"""
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

"""

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:

        def grayCode(n):
            if n == 0:
                return [0]
            if n == 1:
                return [0, 1]
            res = grayCode(n - 1) # get the previous gray code
            # add 2^(n-1) to the reverse of the previous gray code
            return res + [2 ** (n - 1) + i for i in res[::-1]]

        return grayCode(n)

# Time complexity: O(2^n)
# Space complexity: O(2^n)
print(Solution().gryCode(2)) # [0,1,3,2]
