"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 


"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp={}
        def dfs(row,col):
            if row >= rows or col >= cols:
                return float('inf')

            if row == rows-1 and col == cols-1:
                return grid[row][col]
            
            if (row,col) in dp:
                return dp[(row,col)]
            
            minCost = float('inf')

            downCost =grid[row][col]+dfs(row+1,col)
            rightCost =grid[row][col]+dfs(row,col+1)

            minCost = min(downCost,rightCost)

            return minCost
        
        return dfs(0,0)

    def minPathSum2(self, grid: List[List[int]]) -> int:

        rows,cols=len(grid),len(grid[0])

        dp=[ [float('inf') for _ in range(cols)] for  _ in range(rows)]
        dp[0][0]=grid[0][0]

        for row in range(rows):
            for col in range(cols):
                if row-1>=0:
                    dp[row][col]=min(dp[row][col],dp[row-1][col]+grid[row][col])
                if col-1>=0:
                    dp[row][col]=min(dp[row][col],dp[row][col-1]+grid[row][col])


        print(dp)
        return dp[rows-1][cols-1]
    # SPACE OPTIMIZED BOTTOM UP
    def minPathSum3(self,grid:List[List[int]])->int:
        rows,cols=len(grid),len(grid[0])
        dp=[0 for _ in range(cols)]
        dp[0]=grid[0][0]

        for row in range(rows):
            temp=[float('inf')] * cols
            for col in range(cols):
                # base case
                if row == 0 and col == 0:
                    temp[col]=grid[row][col]

                if row-1>=0:
                    # dp[col] is the value from the previous row
                    # top will be taken from the dp array
                    temp[col]=min(temp[col],dp[col]+grid[row][col])
                if col-1>=0:
                    # temp[col] is the value from the current row
                    # left will be taken from the temp array
                    temp[col]=min(temp[col],temp[col-1]+grid[row][col])

            dp=temp

            
        return dp[cols-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
# print(Solution().minPathSum2(grid))
print(Solution().minPathSum3(grid))
