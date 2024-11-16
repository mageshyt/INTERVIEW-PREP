"""
Given an array arr of size n of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7.

Examples:

Input: 
n = 6, arr = [5, 2, 3, 10, 6, 8], sum = 10
Output: 
3
Explanation: 
{5, 2, 3}, {2, 8}, {10} are possible subsets.
Input: 
n = 5, arr = [2, 5, 1, 4, 3], sum = 10
Output: 
3
Explanation: 
{2, 1, 4, 3}, {5, 1, 4}, {2, 5, 3} are possible subsets.
"""

class Solution:
    # TOP DOWN 
    # Time: O(n*sum) | Space: O(n) + O(n) (recursion stack)
    def perfectSum(self, arr, n, sum):
        MOD = 10**9 + 7
        dp={}

        def dfs(idx,target):
            if  idx == 0:
                if (target ==0 and arr[idx]==0):
                   return 2
                if target == 0 or arr[idx] == target:
                    return 1

                return 0

            if (idx,target) in dp:
                return dp[(idx,target)]
            
            notTaken = dfs(idx-1,target)
            taken = 0
            if arr[idx] <= target:
                taken= dfs(idx-1,target-arr[idx])

            dp[(idx,target)] = (taken + notTaken) % MOD

            return dp[(idx,target)]

        return dfs(n-1,sum)

    # BOTTOM UP
    # Time: O(n*sum) | Space: O(n*sum)
    def perfectSum2(self, arr, n, sum):
        MOD = 10**9 + 7
        dp=[[0 for _ in range(sum+1)] for _ in range(n)]


        if arr[0] <= sum and arr[0] != 0:
            dp[0][arr[0]] = 1
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        for i in range(1,n):
            for target in range(sum+1):
                notTaken = dp[i-1][target]
                taken = 0
                if arr[i] <= target:
                    taken = dp[i-1][target-arr[i]]

                dp[i][target] = (taken + notTaken) % MOD



        return dp[n-1][sum]
        
    # SPACE OPTIMIZED
    # Time: O(n*sum) | Space: O(sum)
    def perfectSum3(self, arr, n, sum):
        MOD = 10**9 + 7
        dp=[0]*(sum+1)
        
        if arr[0] <= sum and arr[0] !=0:
            dp[arr[0]] = 1

        if arr[0] == 0:
            dp[0] = 2
        else:
            dp[0] = 1


        for i in range(1,n):
            curr = [0]*(sum+1)
            for target in range(sum+1):
                notTaken = dp[target]
                taken = 0
                if arr[i] <= target:
                    taken = dp[target-arr[i]]

                curr[target] = (taken + notTaken) % MOD

            dp = curr

        return dp[sum]

    
s=Solution()
print(s.perfectSum([5, 2, 3, 10, 6, 8],6,10)) # 3
print(s.perfectSum2([5, 2, 3, 10, 6, 8],6,10)) # 3


arr = [9,7,0,3,9,8,6,5,7,6]
k = 31

print(s.perfectSum(arr,len(arr),k)) # 2
print(s.perfectSum2(arr,len(arr),k)) # 2
print(s.perfectSum3(arr,len(arr),k)) # 2
