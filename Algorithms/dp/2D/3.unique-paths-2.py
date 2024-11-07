"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


"""

from typing import List
class Solution:
    # TOP DOWN 
    # Time : o(2^m*n) | Space : o(m*n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])

        dp={}

        def dfs(row,col):
            # BASE CASE
            if row>=rows or col >=cols or obstacleGrid[row][col] ==1:
                return 0

            if (row,col) in dp:
                return dp[(row,col)]

            if (row,col) == (rows-1,cols-1):
                return 1
            moveRight=dfs(row,col+1)
            moveDown=dfs(row+1,col)


    
            dp[(row,col)]=moveRight+moveDown

            return dp[(row,col)]

        return dfs(0,0)

    # BOTTOM UP
    # Time : o(m*n) | Space : o(m*n)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0 for _ in range(cols)] for _ in range(rows)]

        dp[0][0]=1

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    dp[row][col]=0
                else:
                    if row-1>=0:
                        dp[row][col]+=dp[row-1][col]
                    if col-1>=0:
                        dp[row][col]+=dp[row][col-1]

        return dp[rows-1][cols-1]

    # SPACE OPTIMIZED BOTTOM UP
    # Time : o(m*n) | Space : o(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        dp=[0 for _ in range(cols)]
        dp[0]=1

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    dp[col]=0
                else:
                    if col-1>=0:
                        dp[col]+=dp[col-1]

        return dp[cols-1]

