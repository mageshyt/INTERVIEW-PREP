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
