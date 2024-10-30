"""
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.



"""
from typing import List
from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows,cols=len(grid),len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]


        dp=[[0]*cols for _ in range(rows)]
        dp[0][0]=health-grid[0][0]
queue=deque([(0,0,dp[0][0])]) # (row,col,health) while queue: row,col,health=queue.popleft()

            if (row,col)==(rows-1,cols-1) and health>0:
                return True

            for dx,dy in directions: rowOffset,colOffset=row+dx,col+dy
                if rowOffset<0 or rowOffset>=rows or colOffset<0 or colOffset>=cols:
                    continue

                newHealth=health-grid[rowOffset][colOffset]

                if newHealth<=0:
                    continue


                if newHealth>dp[rowOffset][colOffset]:
                    dp[rowOffset][colOffset]=newHealth
                    queue.append((rowOffset,colOffset,newHealth))

        return False
