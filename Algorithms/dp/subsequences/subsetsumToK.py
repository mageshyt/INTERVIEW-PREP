"""
Given an array of positive integers, arr[] and a value, target, determine if there is a subset of the given set with sum equal to given target. 

Examples:

Input: arr[] = [3, 34, 4, 12, 5, 2], target = 9
Output: true 
Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.
"""

class Solution:
    # TOP DOWN
    # Time: o(n*target) | Space: O(n*target) + (n) (recursion stack)
    def isSubsetSum (self, arr, target): 
        dp={}

        def dfs(idx,target):
            # BASE CASE
            if target == 0:
                return True
            if idx == 0:
                return arr[idx] == target

            # CHOICES

            # 1. Include the current element
            take = False
            if arr[idx] <= target:
                take = dfs(idx-1,target-arr[idx])

            # 2. Exclude the current element
            skip = dfs(idx-1,target)

            dp[(idx,target)] = take or skip

            return dp[(idx,target)]

        return dfs(len(arr)-1,target)

    # BOTTOM UP
    # Time: o(n*target) | Space: O(n*target)

    def isSubsetSum2(self,arr,target):
        n=len(arr)
        dp=[[False for _ in range(target+1)] for _ in range(n)]
        # FILL THE BASE CASE
        for i in range(len(arr)):
            dp[i][0] = True

        if arr[0] <= target:
         dp[0][arr[0]] = True

        for i in range(1,n):
            for target in range(1,target+1):
                take=False
                notTake= dp[i-1][target]
                if arr[i] <= target:
                    take = dp[i-1][target-arr[i]]

                dp[i][target] = take or notTake

        return dp[n-1][target]


print(Solution().isSubsetSum([3, 34, 4, 12, 5, 2],9)) # True
print(Solution().isSubsetSum2([3, 34, 4, 12, 5, 2],9)) # True

print("=================")
ip=open('./input.txt','r')
nums = list(map(int,ip.readline().strip().split()))
target = int(ip.readline().strip())

print(Solution().isSubsetSum(nums,target)) # True
print(Solution().isSubsetSum2(nums,target)) # True
