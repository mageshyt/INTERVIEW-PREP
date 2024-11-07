"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


"""

class Solution:
    # TOP DOWN DP 
    # Time : o(2^m*n) | Space : o(m+n)
    def uniquePaths(self, m: int, n: int) -> int
        dp= {}

        def dfs(row,col):
            if row == m-1 and col == n-1:
                return 1
            if row >= m or col >= n:
                return 0
            if (row,col) in dp:
                return dp[(row,col)]
            right = dfs(row,col+1)
            down = dfs(row+1,col)

            dp[(row,col)] = right+down
            return dp[(row,col)]

        return dfs(0,0)


    # BOTTOM UP DP
    # Time : o(m*n) | Space : o(m*n)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row-1 >= 0:
                    dp[row][col] += dp[row-1][col]
                if col-1 >= 0:
                    dp[row][col] += dp[row][col-1]

        return dp[m-1][n-1]

    # SPACE OPTIMIZED BOTTOM UP DP
    # Time : o(m*n) | Space : o(n)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1

        for row in range(m):
            for col in range(n):
                if col-1 >= 0:
                    dp[col] += dp[col-1]


        return dp[n-1]
