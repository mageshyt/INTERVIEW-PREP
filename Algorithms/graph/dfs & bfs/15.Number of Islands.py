"""
Problem Statement: Given a grid of size NxM (N is the number of rows and M is the number of columns in the grid) consisting of '0's (Water) and ‘1's(Land). Find the number of islands.

Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.


"""

from typing import List

class Solution:
    def numIslands(self,grid:List[List[str]])->int:
        if not grid:
            return 0

        rows,cols = len(grid),len(grid[0])
        visited=set()
        islands = 0

        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

        def dfs(r,c):
            if(
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == '0' or
                (r,c) in visited
            ): 
               return

            visited.add((r,c))

            for dr,dc in directions:
                dfs(r+dr,c+dc)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    islands += 1
                    dfs(i,j)
        return islands






# test the solution

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid)) # 1
print(sol.numIslands(grid2)) # 3
