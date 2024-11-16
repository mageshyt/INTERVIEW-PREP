"""
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.



Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        increasing_run_lengths = [1] * n

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                increasing_run_lengths[i] = increasing_run_lengths[i + 1] + 1

        left, right = 1, n // 2
        result = 0
        while left <= right:
            k = (left + right) // 2
            found = False

            for i in range(n - 2 * k + 1):
                if increasing_run_lengths[i] >= k and increasing_run_lengths[i + k] >= k:
                    found = True
                    break

            if found:
                result = k 
                left = k + 1
            else:
                right = k - 1 

        return result           


print(Solution().maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])) # 3
print(Solution().maxIncreasingSubarrays([2])) # 3

print(Solution().maxIncreasingSubarrays([-3,-19,-8,-16])) # 2
