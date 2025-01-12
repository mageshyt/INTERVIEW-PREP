"""
You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.

The grid contains a value coins[i][j] in each cell:

If coins[i][j] >= 0, the robot gains that many coins.
If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.

Note: The robot's total coins can be negative.

Return the maximum profit the robot can gain on the route.

 

Example 1:

Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]

Output: 8

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 0 coins (total coins = 0).
Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).
Example 2:

Input: coins = [[10,10,10],[10,10,10]]

Output: 40

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 10 coins (total coins = 10).
Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).
©leetcode
"""

from typing import List
import heapq
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        dp= { } # (neutralized, row, col) -> max coins
        rows, cols = len(coins), len(coins[0])

        def dfs(neutralized, row, col):
            if (neutralized, row, col) in dp:
                return dp[(neutralized, row, col)]

            if row <0 or col < 0 or row >= rows or col >= cols:
                return float('-inf')

            if (row, col) == (rows-1, cols-1):
                coins_here = coins[row][col]
                if coins_here >= 0:
                    dp[(neutralized, row, col)] = coins_here
                else:
                    if neutralized > 0:
                        dp[(neutralized, row, col)] = max(0, coins_here)
                    else:
                        dp[(neutralized, row, col)] = coins_here

                return dp[(neutralized, row, col)]

            coins_here = coins[row][col]

            down= dfs(neutralized, row+1, col)
            right = dfs(neutralized, row, col+1) 

            best = max(down, right)

            if coins_here >= 0:
                dp[(neutralized, row, col)] = coins_here + best

            else:
                pay=coins_here + best
                skip=float('-inf')

                if neutralized > 0:
                    down2 = dfs(neutralized-1, row+1, col)
                    right2 = dfs(neutralized-1, row, col+1)

                    skip = max(down2, right2)

                dp[(neutralized, row, col)] = max(pay, skip)

            return dp[(neutralized, row, col)]
        return dfs(2, 0, 0)

sol = Solution()
print(sol.maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]])) # 8
print(sol.maximumAmount([[10,10,10],[10,10,10]])) # 40
print(sol.maximumAmount([[0,0,0],[0,0,0]])) # 0
print(sol.maximumAmount([[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]])) # 0




