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

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum2(grid))
