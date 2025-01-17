"""
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 
"""

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[1] * len(nums)
        freq=[1] * len(nums)

        for i in range(len(nums)):
            for prev in range(0,i):
                if nums[prev] < nums[i] and dp[i] < dp[prev]+1:
                    dp[i]=dp[prev]+1
                    freq[i]=freq[prev]

                elif nums[prev] < nums[i] and dp[i] == dp[prev]+1:
                    freq[i]+=freq[prev]

        maxi=max(dp)

        return sum([freq[i] for i in range(len(nums)) if dp[i] == maxi])

s=Solution()

print(s.findNumberOfLIS([1,3,5,4,7])) # 2
