"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:
"""

from typing import List

class Solution:
    # TOP DOWN

    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        n=len(prices)

        def dfs(idx,buy):
            if idx >= n:
                return 0

            if (idx,buy) in dp:
                return dp[(idx,buy)]

            if buy:
                # buy
                buy_=dfs(idx+1,False)-prices[idx]
                no_buy=dfs(idx+1,True)
                dp[(idx,buy)]=max(buy_,no_buy)

            else:
                # sell
                sell=dfs(idx+1,True)+prices[idx]
                no_sell=dfs(idx+1,False)
                dp[(idx,buy)]=max(sell,no_sell)

            return dp[(idx,buy)]

        return dfs(0,True)

    # BOTTOM UP

    def maxProfit2(self,prices:List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]

        # fill the base case
        dp[n][0]=dp[n][1]=0

        for i in range(n-1,-1,-1):
            for buy in [0,1]:
                if buy:
                    # buy
                    dp[i][buy]=max(dp[i+1][0]-prices[i],dp[i+1][1])

                else:
                    # sell
                    dp[i][buy]=max(dp[i+1][1]+prices[i],dp[i+1][0])

        return dp[0][1]

    # BOTTOM UP OPTIMIZED

    def maxProfit3(self,prices:List[int]) -> int:
        n=len(prices)

        dp=[0]*2
        cur=[0]*2

        for i in range(n-1,-1,-1):
            for buy in [0,1]:
                if buy:
                    # buy
                    cur[buy]=max(dp[0]-prices[i],dp[1])

                else:
                    # sell
                    cur[buy]=max(dp[1]+prices[i],dp[0])

            dp=cur[:]

        return dp[1]
s=Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 7
print(s.maxProfit2([7,1,5,3,6,4])) # 7
print(s.maxProfit3([7,1,5,3,6,4])) # 7
        
