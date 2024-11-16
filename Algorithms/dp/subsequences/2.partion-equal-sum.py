"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List

class Solution:
    # TOP DOWN DP
    # time complexity O(N*sum) | space complexity O(N*sum)
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp={}

        def dfs(index, target):
            if target == 0:
                return True
            
            if index ==0:
                return nums[0] == target


            if (index,target) in dp:
                return dp[(index,target)]

            notTaken = dfs(index-1,target)
            taken = False

            if nums[index] <= target:
                taken = dfs(index-1,target-nums[index])

            dp[(index,target)] = taken or notTaken


            return dp[(index,target)]


    # SPACE OPTIMIZED
    # time complexity O(N*sum) | space complexity O(sum)

    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp=[False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target,num-1,-1):
                dp[i] = dp[i] or dp[i-num]

        return dp[target]


ip=open('./input.txt','r')
nums = list(map(int,ip.readline().strip().split()))
target = int(ip.readline().strip())

print(Solution().canPartition(nums)) # True
