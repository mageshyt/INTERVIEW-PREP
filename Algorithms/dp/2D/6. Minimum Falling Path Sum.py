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
    # Time: O(n^2) | Space: O(n^2)
    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp=[[float('inf') for _ in range(cols)] for _ in range(rows)]

        for col in range(cols):
            dp[0][col]=matrix[0][col]
        
        for row in range(1,rows):
            for col in range(cols):
                up=matrix[row][col] + dp[row-1][col]
                left=right=float('inf')
                if col > 0:
                    left=matrix[row][col] + dp[row-1][col-1]
                if col < cols-1:
                    right=matrix[row][col] + dp[row-1][col+1]

                dp[row][col]=min(up,left,right)



        return min(dp[-1])

    # SPACE OPTIMIZED 
    # Time: O(n^2) | Space: O(1)
    def minFallingPathSum3(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])

        for row in range(1,rows):
            for col in range(cols):
                up=matrix[row][col] + matrix[row-1][col]
                left=right=float('inf')
                if col > 0:
                    left=matrix[row][col] + matrix[row-1][col-1]
                if col < cols-1:
                    right=matrix[row][col] + matrix[row-1][col+1]

                matrix[row][col]=min(up,left,right)

        return min(matrix[-1])


print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])) # 12
print(Solution().minFallingPathSum2([[2,1,3],[6,5,4],[7,8,9]])) # 12
print(Solution().minFallingPathSum3([[2,1,3],[6,5,4],[7,8,9]])) # 12
