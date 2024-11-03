"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""

from typing import List

class Solution:
    # TOP DOWN 
    # Time : (2^n) | Space : O(n)
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(house):
            # base case
            if house < 0:
                return 0

            if house == 0:
                return nums[0]

            if house in memo:
                return memo[house]

            robCurrentHouse = nums[house] + dfs(house-2)
            skipCurrentHouse = dfs(house-1)

            memo[house] = max(robCurrentHouse,skipCurrentHouse)

            return memo[house]
        
        return dfs(len(nums)-1)
    
    # BOTTOM UP
    # Time : O(n) | Space : O(n)
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(
                dp[i-1],
                dp[i-2]+nums[i]
            )

        return dp[-1]
    # SPACE OPTIMIZED
    # Time : O(n) | Space : O(1)
    def rob3(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        prev,curr = nums[0],max(nums[0],nums[1])

        for i in range(2,n):
            prev,curr = curr,max(curr,prev+nums[i])

        return curr

print(Solution().rob([2,7,9,3,1])) # 12
print(Solution().rob2([2,7,9,3,1])) # 12
print(Solution().rob3([2,7,9,3,1])) # 12
