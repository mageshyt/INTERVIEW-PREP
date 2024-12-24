"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

"""


# Same as 3.Best Time to Buy and Sell Stock III.py but with k transactions
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp={}

        n=len(prices)

        def dfs(idx,buy,cap):
            if cap ==0 or idx ==n:
                return 0

            if (idx,buy,cap) in dp:
                return dp[(idx,buy,cap)]

            if buy :
                buy_stocks= -prices[idx] + dfs(idx+1,False,cap)
                no_buy=dfs(idx+1,True,cap)

                dp[(idx,buy,cap)]=max(buy_stocks,no_buy)

            else:
                sell_stock= prices[idx] + dfs(idx+1,True,cap-1)
                no_sell=dfs(idx+1,False,cap)

                dp[(idx,buy,cap)]=max(sell_stock,no_sell)

            return dp[(idx,buy,cap)]
        
        return dfs(0,True,k)

        
    # Bottom Up optimization
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)


        dp=[[0]*(k+1) for _ in range(2)]
        cur=[[0]*(k+1) for _ in range(2)]



        for i in range(n-1,-1,-1):
            for buy in [0,1]:
                for cap in range(1,k+1):
                    if buy:
                        buy_stock= -prices[i] + dp[0][cap]
                        no_buy=dp[1][cap]

                        cur[buy][cap]=max(buy_stock,no_buy)

                    else:

                        sell_stock= prices[i] + dp[1][cap-1]
                        no_sell=dp[0][cap]

                        cur[buy][cap]=max(sell_stock,no_sell)

            dp,cur=cur,dp

        return dp[1][k]


s=Solution()
print(s.maxProfit(2,[3,2,6,5,0,3])) #7
print(s.maxProfit(2,[2,4,1])) #2


