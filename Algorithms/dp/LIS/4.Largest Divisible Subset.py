"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 
"""

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp=[1]*len(nums)
        hash={}

        # sort the array
        nums.sort()
        idx=0

        for i in range(len(nums)):
            hash[i]=i
            for j in range(0,i):
                # if teh current number is divisible by the previous number
                if nums[i] % nums[j] == 0 and dp[i] < dp[j]+1:
                    dp[i]=max(dp[i],dp[j]+1)
                    hash[i]=j

            if dp[i] > dp[idx]:
                idx=i
        res=[]

        while hash[idx] != idx:
            res.append(nums[idx])
            idx=hash[idx]

        res.append(nums[idx])

        return res

s=Solution()
print(s.largestDivisibleSubset([1,2,3])) # [1,2]
print(s.largestDivisibleSubset([4,8,10,240])) # [1,2]




