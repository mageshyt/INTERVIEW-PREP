"""
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum
Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.
Expected Time Complexity: O(n*k)
Expected Auxilary Space: O(n)
"""

from typing import List
class Solution:
    # TOP DOWN 
    # Time : O(n*k) | Space : O(n)
    def frogWithKJump(self,n:int,height:List[int],k:int)->int:
        dp={}

        def dfs(i):

            if i == 0:
                return 0
            if i in dp:
                return dp[i]

            minJump = float('inf')

            for j in range(1,k+1):
                if i-j >= 0:
                    jump= dfs(i-j) + abs(height[i]-height[i-j])
                    minJump = min(minJump,jump)

            dp[i] = minJump

            return minJump

        return dfs(n-1)

    # BOTTOM UP
    # Time : O(n*k) | Space : O(n)
    def minimizeCost(self,k:int,height)->int:
        n=len(height)
        dp = [0]*n

        for i in range(1,n):
            dp[i] = float('inf')
            for j in range(1,k+1):
                if i-j >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i-j]+abs(height[i]-height[i-j])
                    )

        return dp[-1]

print(Solution().frogWithKJump(4,[10,20,30,10],2)) # 20
