"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List
class Solution:
    # TOP DOWN
    def maxProfit(self, prices: List[int]) -> int:
        dp={} # (idx,buy,cap) -> profit
        n=len(prices) 

        def dfs(idx,buy,cap):

            # base case

            if cap ==0 or idx ==n:
                return 0

            
            if (idx,buy,cap) in dp:
                return dp[(idx,buy,cap)]

            if buy:
                buy_stock= -prices[idx] + dfs(idx+1,False,cap)

                no_buy=dfs(idx+1,True,cap)

                dp[(idx,buy,cap)]=max(buy_stock,no_buy)

            else:
                sell_stock= prices[idx] + dfs(idx+1,True,cap-1)

                no_sell=dfs(idx+1,False,cap)

                dp[(idx,buy,cap)]=max(sell_stock,no_sell)

            return dp[(idx,buy,cap)]

        return dfs(0,True,2)

    # BOTTOM UP

    def maxProfit2(self,prices:List[int]) -> int:
        n=len(prices)

        dp=[[[0]*3 for _ in range(2)] for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for buy in [0,1]:
                for cap in range(1,3):
                    if buy:
                        buy_stock= -prices[i] + dp[i+1][0][cap]
                        no_buy=dp[i+1][1][cap]

                        dp[i][buy][cap]=max(buy_stock,no_buy)

                    else:

                        sell_stock= prices[i] + dp[i+1][1][cap-1]
                        no_sell=dp[i+1][0][cap]

                        dp[i][buy][cap]=max(sell_stock,no_sell)

        return dp[0][1][2]

    # BOTTOM UP OPTIMIZED
    def maxProfit3(self,prices:List[int]) -> int:
        n=len(prices)
        dp=[[0]*3 for _ in range(2)]
        cur=[[0]*3 for _ in range(2)]

        for i in range(n-1,-1,-1):
            for buy in [0,1]:
                for cap in range(1,3):
                    if buy:
                        buy_stock= -prices[i] + dp[0][cap]
                        no_buy=dp[1][cap]

                        cur[buy][cap]=max(buy_stock,no_buy)

                    else:

                        sell_stock= prices[i] + dp[1][cap-1]
                        no_sell=dp[0][cap]

                        cur[buy][cap]=max(sell_stock,no_sell)

            dp,cur=cur,dp

        return dp[1][2]




s=Solution()
print(s.maxProfit2([3,3,5,0,0,3,1,4])) #6
print(s.maxProfit3([3,3,5,0,0,3,1,4])) #6
