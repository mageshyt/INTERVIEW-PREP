"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}

        def dfs(amt,index):
            # base case
            if amt == 0:
                return 0

            if amt < 0 or index >= len(coins):
                return float('inf')

            if (amt,index) in dp:
                return dp[(amt,index)]

            # EXPLORE ALL POSSIBLE MOVES
            count=float('inf')
            count = min(count,1+dfs(amt-coins[index],index))

            count = min(count,dfs(amt,index+1))

            dp[(amt,index)]=count

            return dp[(amt,index)]


        res=dfs(amount,0)

        return res if res != float('inf') else -1

# Time : O(N*M) | Space : O(N*M)
print(Solution().coinChange([1,2,5],11)) # 3