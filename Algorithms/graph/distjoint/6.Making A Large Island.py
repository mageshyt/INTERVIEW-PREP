"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

"""

from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        points=[]
        rows,cols=len(grid),len(grid[0])
        maxArea=0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    points.append((row,col))

        if not points:
            return rows*cols


        def bfs(row,col):
            visited=set()
            q=deque([(row,col)])
            area=0

            while q:
                r,c=q.popleft()

                if (r,c) in visited:
                    continue

                visited.add((r,c))
                area+=1

                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc=r+dr,c+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        q.append((nr,nc))

            return area

        
        for row,col in points:
            grid[row][col]=1
            maxArea=max(maxArea,bfs(row,col))
            grid[row][col]=0


        return maxArea

grid = [[1,0],[1,1]]

print(Solution().largestIsland(grid))



