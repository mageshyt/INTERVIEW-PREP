"""
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.


"""
from typing import List
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if 2*k > n:
            return False

        def isIncreasing(nums):
            if len(nums) != k:
                return False
            for i in range(1,len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True

        for i in range(n-k):
            if isIncreasing(nums[i:i+k]) and isIncreasing(nums[i+k:i+2*k]):
                return True

        return False
print(Solution().hasIncreasingSubarrays([2,5,7,8,9,2,1,4,3,1],3)) # True
print(Solution().hasIncreasingSubarrays([-3,-19,-8,-16],2)) # False
