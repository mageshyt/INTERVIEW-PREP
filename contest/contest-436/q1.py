"""

Q1. Sort Matrix by Diagonals
Medium
3 pt.
You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.
"""

from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
 

        # diagonal from bottom left
        for i in range(n):
            temp = []
            x = i
            y = 0
            while x < n and y < m:
                temp.append(grid[x][y])
                x += 1
                y += 1
            temp.sort(reverse=True)
            x = i
            y = 0
            idx = 0
            while x < n and y < m:
                grid[x][y] = temp[idx]
                x += 1
                y += 1
                idx += 1

        # diagonal from top right
        for i in range(1, m):
            temp = []
            x = 0
            y = i
            while x < n and y < m:
                temp.append(grid[x][y])
                x += 1
                y += 1
            temp.sort()
            x = 0
            y = i
            idx = 0
            while x < n and y < m:
                grid[x][y] = temp[idx]
                x += 1
                y += 1
                idx += 1
        
        return grid


solution = Solution()
print(solution.sortMatrix([[1,7,3],[9,8,2],[4,5,6]]))  # Output: [[8,2,3],[9,6,7],[4,5,1]]
