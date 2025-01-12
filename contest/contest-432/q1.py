"""


You are given an m x n 2D array grid of positive integers.

Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.

Zigzag pattern traversal is defined as following the below actions:

Start at the top-left cell (0, 0).
Move right within a row until the end of the row is reached.
Drop down to the next row, then traverse left until the beginning of the row is reached.
Continue alternating between right and left traversal until every row has been traversed.
Note that you must skip every alternate cell during the traversal.

Return an array of integers result containing, in order, the value of the cells visited during the zigzag traversal with skips.

"""
from typing import List
from collections import deque
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        result = []

        skip = False

        for row in range(rows):
            if row %2 == 0:
                for col in range(cols):
                    if not skip:
                        result.append(grid[row][col])
                    skip = not skip
            else:
                for col in range(cols-1, -1, -1):
                    if not skip:
                        result.append(grid[row][col])
                    skip = not skip

        return result
sol = Solution()
print(sol.zigzagTraversal([[1,2],[3,4]])) # [1, 3, 4, 6, 7, 9]
print(sol.zigzagTraversal([[2,1],[2,1],[2,1]]))


