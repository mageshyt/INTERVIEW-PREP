from math import ceil, log
from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # base case :
        if k == 1:
            return "a"
        start=1
        n=len(operations)
        for i in range(n):
            start = start<<1
            if start >= k:
                break

        # print("START>>",start)
        changes=0

        for j in range(i,-1,-1):
            if k > start //2:
                changes+=operations[j]
                k -= start //2
            start = start //2

        # print("CHANGES>>",changes)
        return chr(ord("a")+changes % 26) 

# Time complexity: O(n)


# Example test case
solution = Solution()
print(solution.kthCharacter(5, [0, 0,0]))  # Expected output: 'a', modifies to "aaaa"
print("----------------")
print(solution.kthCharacter(10, [0, 1,0,1]))  # Expected output: 'b', modifies to "aa" -> "bb"
print(solution.kthCharacter(4, [0, 1]))  # Expected output: 'b', modifies to "aa" -> "bb"
