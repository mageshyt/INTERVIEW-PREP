"""
You are given an n rows and m cols matrix grid representing a field of chocolates where grid[i][j] represents the number of chocolates that you can collect from the (i, j) cell.

You have two robots that can collect chocolates for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of chocolates collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all chocolates, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the chocolates.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.
Example:

Input:
n = 4, m = 3
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output:
24
Explanation:
Path of robot #1 and #2 are described in color green and blue respectively. Chocolates taken by Robot #1, (3 + 2 + 5 + 2) = 12. Chocolates taken by Robot #2, (1 + 5 + 5 + 1) = 12. Total of Chocolates: 12 + 12 = 24.
"""


class Solution:
    # TOP DOWN DP
    def solve(self, n, m, grid):
        dp={}

        def dfs(row,col1,col2):
            # base case OUT OF BOUNDS
            if col1 < 0 or col2<0 or col1 >= m or col2 >= m:
                return float('-inf')

            # base case DESTINATION
            if row == n-1:
                # SAME ENDING
                if col1 == col2:
                    return grid[row][col1]

                return grid[row][col1] + grid[row][col2]


            if (row,col1,col2) in dp:
                return dp[(row,col1,col2)]

            # EXPLORE ALL POSSIBLE MOVES

            maxChoc=float('-inf')

            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    maxChoc=max(maxChoc,dfs(row+1,col1+i,col2+j))

            # ADD THE CURRENT CHOCOLATE
            if col1 == col2:
                maxChoc += grid[row][col1]

            else:
                maxChoc += grid[row][col1] + grid[row][col2]

            dp[(row,col1,col2)]=maxChoc


            return dp[(row,col1,col2)]

        return dfs(0,0,m-1)


    # BOTTOM UP DP

    def solve2(self,n,m,grid):
        # 3D DP
        dp=[[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        # BASE CASE
        for j1 in range(m):
            for j2 in range(m):
                if j1==j2:
                    dp[n-1][j1][j2]=grid[n-1][j1]

                else:
                    dp[n-1][j1][j2]=grid[n-1][j1]+grid[n-1][j2]

        
        # EXPLORE ALL POSSIBLE MOVES

        for i in range(n-2,-1,-1):
            for j1 in range(m):
                for j2 in range(m):
                    maxChoc=float('-inf')

                    for k1 in [-1,0,1]:
                        for k2 in [-1,0,1]:
                            if j1+k1>=0 and j1+k1<m and j2+k2>=0 and j2+k2<m:
                                maxChoc=max(maxChoc,dp[i+1][j1+k1][j2+k2])

                    if j1==j2:
                        dp[i][j1][j2]=maxChoc+grid[i][j1]
                    else:
                        dp[i][j1][j2]=maxChoc+grid[i][j1]+grid[i][j2]

        return dp[0][0][m-1]
        



n = 4
m = 3
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(Solution().solve2(n,m,grid)) # 24


ip=open('./input.txt','r')

n,m=map(int,ip.readline().strip().split())
grid=[]
for _ in range(n):
    grid.append(list(map(int,ip.readline().strip().split())))

print(Solution().solve2(n,m,grid)) # 24

