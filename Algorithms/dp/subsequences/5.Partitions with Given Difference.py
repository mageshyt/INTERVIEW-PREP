"""
Given an array arr, partition it into two subsets(possibly empty) such that each element must belong to only one subset. Let the sum of the elements of these two subsets be S1 and S2. 
Given a difference d, count the number of partitions in which S1 is greater than or equal to S2 and the difference between S1 and S2 is equal to d. Since the answer may be large return it modulo 109 + 7.

Example 1:

Input:
n = 4
d = 3
arr[] =  { 5, 2, 6, 4}
Output: 1
Explanation:
There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3
"""

from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        MOD = 10**9 + 7
        total = sum(arr)
        target = (d + total) // 2

        if (d + total) % 2 != 0:
            return 0
        dp={}  
        def dfs(idx,target):
            if idx==0:
                if target ==0 and arr[0] ==0:
                    return 2

                if target ==0 or arr[idx] == target:
                    return 1

                return 0
            if (idx,target) in dp:
                return dp[(idx,target)]

            take=0
            if arr[idx] <=target:
                take=dfs(idx-1,target-arr[idx])

            notTake=dfs(idx-1,target)

            dp[(idx,target)]=(take+notTake) % MOD

            return take+notTake

        return dfs(n-1,target)


    def countPartitions2(self, n : int, d : int, arr : List[int]) -> int:
        MOD = 10**9 + 7
        total = sum(arr)
        target = (d + total) // 2

        if (d + total) % 2 != 0:
            return 0


        dp=[[0]*(target+1) for _ in  range(n)]

        if arr[0] <= target and arr[0] != 0:
            dp[0][arr[0]] = 1
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        for i in range(1,n):
            for j in range(target+1):
                take=0  
                if arr[i] <= j:
                    take=dp[i-1][j-arr[i]]

                notTake=dp[i-1][j]

                dp[i][j]=(take+notTake) % MOD

                    

        return dp[n-1][target]
    
    # SPACE OPTIMIZED

    def countPartitions3(self, n : int, d : int, arr : List[int]) -> int:
        MOD=10**9+7

        total = sum(arr)
        target = (d + total) // 2

        if (d + total) % 2 != 0:
            return 0

        prev=[0]*(target+1)

        if arr[0] <= target and arr[0] != 0:
            prev[arr[0]] = 1

        if arr[0] == 0:
            prev[0] = 2

        else:
            prev[0] = 1

        for i in range(1,n):
            curr=[0]*(target+1)
            for j in range(target+1):
                take=0  
                if arr[i] <= j:
                    take=prev[j-arr[i]]

                notTake=prev[j]

                curr[j]=(take+notTake) % MOD

            prev=curr
        return prev[target]
        
s=Solution()

print(s.countPartitions(4,0,[1,1,1,1]))
print(s.countPartitions2 (4,0,[1,1,1,1]))
print(s.countPartitions3(4,0,[1,1,1,1]))
        



