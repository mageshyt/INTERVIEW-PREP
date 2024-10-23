"""
iven an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
"""
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols=len(mat),len(mat[0])

        q = deque() # (row,col,distance)

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row,col,0))
                else:
                    # set the cell to infinity because we will update it later
                    mat[row][col] = float('inf')

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:

            # get the row,col and distance
            row,col,distance = q.popleft()

            for dx,dy in directions:
                newRow = row + dx
                newCol = col + dy

                # check if the new cell is within the bounds

                if 0<=newRow<rows and 0<=newCol<cols and mat[newRow][newCol] > distance+1:
                    mat[newRow][newCol] = distance+1
                    q.append((newRow,newCol,distance+1))

        return mat

print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]])) # [[0,0,0],[0,1,0],[0,0,0]]
        
