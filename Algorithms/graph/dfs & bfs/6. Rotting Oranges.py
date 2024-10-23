"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find  no of fresh oranges and rotten oranges
        fresh = 0
        rotten = deque()

        rows=len(grid)
        cols=len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rotten.append((row,col))

        # if no fresh oranges return 0
        if fresh == 0:
            return 0

        # if no rotten oranges return -1
        if not rotten:
            return -1



        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        # go through the rotten oranges and mark the fresh oranges as rotten
        minutes = 0

        while rotten and fresh > 0:
            minutes+=1

            for _ in range(len(rotten)):
                row,col = rotten.popleft()

                for dx,dy in directions:
                    newRow = row + dx
                    newCol = col + dy

                    # if the new cell is a fresh orange mark it as rotten
                    if 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        rotten.append((newRow,newCol))

        return minutes-1 if fresh == 0 else -1


# Time complexity : O(N) where N is the number of cells in the grid
# Space complexity : O(N) where N is the number of cells in the grid

