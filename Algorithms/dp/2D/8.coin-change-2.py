"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.

Example 1:

Input: amount = 4, coins = [1,2,3]

Output: 4
Explanation:

1+1+1+1 = 4
1+1+2 = 4
2+2 = 4
1+3 = 4
Example 2:

Input: amount = 7, coins = [2,4]

Output: 0
"""
from typing import List
class Solution:
    # BOTTOM UP DP
    # Time : O(N*M) | Space : O(N)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0]=1

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]

    # TOP DOWN DP
    # Time : O(N*M) | Space : O(N*M)
    def change2(self,amount:int,coins:List[int]):
        dp={}

        def dfs(amt,index):
            # base case
            if amt == 0:
                return 1

            if amt < 0 or index >= len(coins):
                return 0

            if (amt,index) in dp:
                return dp[(amt,index)]

            # EXPLORE ALL POSSIBLE MOVES
            count=0
            count += dfs(amt-coins[index],index) # TAKE THE CURRENT COIN

            count += dfs(amt,index+1) # SKIP THE CURRENT COIN

            dp[(amt,index)]=count

            return count

        return dfs(amount,0)

print(Solution().change(4,[1,2,3])) # 4
print(Solution().change2(4,[1,2,3])) # 4

