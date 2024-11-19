"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

from typing import List
class Solution:
    # TOP DOWN DP
    # Time : O(N*M) | Space : O(N*M)
    def change(self,amount:int,coins:List[int]):
        dp={} # (target,idx) -> no of ways

        def dfs(idx,target):
            # print(idx)
            if target ==0:
                return 1
            
            # base -1
            if idx==0:
                return 1 if target %  coins[idx]  ==0 else 0

            if (target,idx) in dp:
                return dp[(target,idx)]

            take=0

            if coins[idx]<=target:
                take=dfs(idx,target-coins[idx])
            notTake=dfs(idx-1,target)

            dp[(target,idx)]=notTake+take
            return dp[(target,idx)]

        return dfs(len(coins)-1,amount)

    # BOTTOM UP

    # Time : O(N*M) | Space : O(N*M)
    def change2(self,amount:int,coins:List[int]):
        n=len(coins)
        dp=[[0]*(amount+1) for _ in  range(n)]

        for i in range(amount+1):
            if i % coins[0]==0:
                dp[0][i]=1


        for idx in range(1,n):
            for target in range(amount+1):
                take=0
                notake=dp[idx-1][target]

                if coins[idx] <=target:
                    take=dp[idx][target - coins[idx]]

                dp[idx][target]=take+notake
        return dp[n-1][amount]

    # SPACE OPTMIZED

    def change3(self,amount:int,coins:List[int]):
        n=len(coins)
        prev=[0] * (amount+1)

        for i in range(amount+1):
            if i % coins[0]==0:
                prev[i]=1


        for idx in range(1,n):
            curr=[0] * (amount+1)
            for target in range(amount+1):

                take=0
                noTake=prev[target]

                if coins[idx] <=target:
                    take=curr[target-coins[idx]]

                curr[target]=take+noTake

            prev=curr

        return prev[amount]


s=Solution()
print(s.change(5,[1,2,5]))
print(s.change2(5,[1,2,5]))
print(s.change3(5,[1,2,5]))
