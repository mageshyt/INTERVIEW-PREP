
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited = set()

        def dfs(row,col):

            if (row,col) in visited:
                return

            # mark the cell as visited
            visited.add((row,col))

            # go through the neighbors 
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                newRow = row + dx
                newCol = col + dy

                # mark the cell as visited if its a valid cell 
                if 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol] == 1:
                    dfs(newRow,newCol)

        # start the dfs from the boundary cells
        for row in range(rows):
            for col in range(cols):

                if (row==0 or row==rows-1 or col==0 or col==cols-1) \
                    and grid[row][col] == 1:
                    dfs(row,col)

        # count the number of enclaves
        enclaves = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    enclaves += 1

        return enclaves

