"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
"""

from typing import List
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            for num in nums[i]:
                if num not in hash_map:
                    hash_map[num] = 1
                else:
                    hash_map[num] += 1

        res = []
        for key in hash_map:
            if hash_map[key] == len(nums):
                res.append(key)

        return sorted(res)


