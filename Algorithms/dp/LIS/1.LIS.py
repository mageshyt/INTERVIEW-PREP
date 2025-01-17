"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

"""

from typing import List

class Solution:
    # TOP DOWN
    # Time: O(n^2) | Space: O(n^2) + O(n) = O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {} # (prev,idx) -> length

        def dfs(prev,idx):
            if idx == len(nums):
                return 0

            if (prev,idx) in dp:
                return dp[(prev,idx)]

            noPick=dfs(prev,idx+1) # prev stays the same, idx moves to the right

            pick=0
            if prev == -1 or nums[idx] > nums[prev]:
                pick=dfs(idx,idx+1)+1

            dp[(prev,idx)]=max(noPick,pick)

            return dp[(prev,idx)]

        return dfs(-1,0)

    # BOTTOM UP
    # Time: O(n^2) | Space: O(n)
    def lengthOfLIS(self,nums)->int:
        n=len(nums)
        dp=[1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)
s=Solution()

print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4

