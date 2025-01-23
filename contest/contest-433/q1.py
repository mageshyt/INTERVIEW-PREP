"""
You are given an integer array nums of size n. For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).

Return the total sum of all elements from the subarray defined for each index in the array.

A subarray is a contiguous non-empty sequence of elements within an array.
 ©leetcode
"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total=0

        n=len(nums)

        for i in range(n):
            start=max(0,i-nums[i])
            total+=sum(nums[start:i+1])

        return total

s=Solution()
print(s.subarraySum([1,2,3,4])) # 20
print(s.subarraySum([2]))
print(s.subarraySum([2,3,1]))
