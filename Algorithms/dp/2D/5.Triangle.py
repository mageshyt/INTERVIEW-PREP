"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
"""
from typing import List
class Solution:
    # TOP DOWN
    # Time O(n^2) | Space O(n^2)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows,cols=len(triangle),len(triangle[-1])
dp={}

        # TARGET : (0,0) -> (rows-1,cols-1) 

        def dfs(row,col):
            # base case
            if row >= rows or col >= cols:
                return float('inf')
            # if we reach the last row
            if row == rows-1:
                return triangle[row][col]

            if (row,col) in dp:
                return dp[(row,col)]

            downCost = triangle[row][col]+dfs(row+1,col)
            rightCost = triangle[row][col]+dfs(row+1,col+1)

            dp[(row,col)]=min(downCost,rightCost)


            return dp[(row,col)]

        return dfs(0,0)

    # BOTTOM UP
    # Time O(n^2) | Space O(n^2)
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        rows,cols=len(triangle),len(triangle[-1])
        dp=[[float('inf') for _ in range(cols)] for _ in range(rows)]

        # TARGET : (rows-1,cols-1) -> (0,0)
        # Fill the base case
        for col in range(cols):
            dp[rows-1][col]=triangle[rows-1][col]

        for row in range(rows-2,-1,-1):
            for col in range(row,-1,-1):
                downCost = triangle[row][col]+dp[row+1][col]
                rightCost = triangle[row][col]+dp[row+1][col+1]

                dp[row][col]=min(downCost,rightCost)


        return dp[0][0] # return the top element
    # SPACE OPTIMIZED BOTTOM UP
    # Time O(n^2) | Space O(n)
    def minimumTotal3(self,triangle):
        dp=[0] * (len(triangle) +1)

        for row in reversed(triangle):
            print(row)
            for col in range(len(row)):
                dp[col]=row[col]+min(dp[col],dp[col+1])

        return dp[0]
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(Solution().minimumTotal2([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(Solution().minimumTotal3([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11


        
