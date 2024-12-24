"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0

"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp={} # (idx,isDown,buy)
        n=len(prices)

        # buying or selling state
            # buy -> idx +1
            # sell -> i+2 because we have to cooldown after buying
        def dfs(idx,buy):
            if idx >=n:
                return 0

            if (idx,buy) in dp:
                return dp[(idx,buy)]

            if buy:
                buy_stock=-prices[idx]+dfs(idx+1,not buy)
                cooldown=dfs(idx+1,buy)

                dp[(idx,buy)]=max(buy_stock,cooldown)

            else:
                # move to next day if we are in selling state
                sell_stock=prices[idx]+dfs(idx+2,not buy)
                no_sell=dfs(idx+1,buy)

                dp[(idx,buy)]=max(sell_stock,no_sell)


            return dp[(idx,buy)]

        return dfs(0,True)

    # bottom up
    def maxProfit(self,prices):
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)] # 2 states buy or sell

        for idx in range(n-1,-1,-1):
            for buy in [0,1]:
                # we are going from back to front
                if buy:
                    # buy
                    buy_stock=-prices[idx]+dp[idx+1][0]
                    cooldown=dp[idx+1][1]

                    dp[idx][buy]=max(buy_stock,cooldown)

                else:
                    # sell
                    sell_stock=prices[idx]+dp[idx+2][1]
                    no_sell=dp[idx+1][0]

                    dp[idx][buy]=max(sell_stock,no_sell)
                    
                    
        return dp[0][1]
s=Solution()

print(s.maxProfit([1,2,3,0,2]))
print(s.maxProfit([4,9,0,4,10]))


        
