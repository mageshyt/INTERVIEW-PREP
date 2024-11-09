"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
"""
from typing import List
class Solution:
    # TOP DOWN 
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp={}
        direction = [(1,0),(1,1),(1,-1)]

        def dfs(row,col):
            # base case
            if row >= rows or col >= cols:
                return float('inf')

            if row == rows-1:
                return matrix[row][col]
            
            if (row,col) in dp:
                return dp[(row,col)]

            minCost = float('inf')

            for r,c in direction:
                newRow,newCol = row+r,col+c
                if 0 <= newRow < rows and 0 <= newCol < cols:
                    minCost = min(minCost,matrix[row][col]+dfs(newRow,newCol))

            dp[(row,col)]=minCost

            return dp[(row,col)]

        return min(dfs(0,col) for col in range(cols))
    # BOTTOM UP
    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp=[[float('inf') for _ in range(cols)] for _ in range(rows)]

        for col in range(cols):
            dp[rows-1][col]=matrix[rows-1][col]
        
        direction = [(1,0),(1,1),(1,-1)]

        for row in range(rows-2,-1,-1):
            for col in range(cols):
                for r,c in direction:
                    newRow,newCol = row+r,col+c
                    if 0 <= newRow < rows and 0 <= newCol < cols:
                        dp[row][col]=min(dp[row][col],matrix[row][col]+dp[newRow][newCol])

        return min(dp[0])
print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])) # 12
print(Solution().minFallingPathSum2([[2,1,3],[6,5,4],[7,8,9]])) # 12
