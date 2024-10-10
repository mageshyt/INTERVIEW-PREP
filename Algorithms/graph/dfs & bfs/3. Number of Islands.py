"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0]) # rows and columns
        islands=0   
        visited=set() # visited set
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(row,col):
            queue=deque([(row,col)]) # put the starting point in the queue

            visited.add((row,col)) # add them to the visited set

            while queue:
                r,c=queue.popleft()
                
                for dx,dy in directions:
                    rowOffset=r+dx
                    colOffset=c+dy

                    if 0<=rowOffset<rows and 0<=colOffset<cols and\
                        grid[rowOffset][colOffset]=='1' and\
                        (rowOffset,colOffset) not in visited:
                        queue.append((rowOffset,colOffset))
                        visited.add((rowOffset,colOffset))

        for row in range(rows):
            for col in range(cols): 
                # if the cell is a land and not visited
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    islands+=1

        return islands


print("TEST CASE")
grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
      ]
grid2=[["1","1","0","0","0"],
       ["1","1","0","0","0"],
       ["0","0","1","0","0"],["0","0","0","1","1"]
       ]
s=Solution()

print(s.numIslands(grid))
print(s.numIslands(grid2))
