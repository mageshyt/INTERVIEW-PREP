"""
Given an array of integers, nums, and an integer k, the task is to find the total number of subarrays whose sum is divisible by k. A subarray is a contiguous portion of the array.


Examples:
Input: nums = [3, 1, 4, 1], k = 3

Output: 3

Explanation: The subarrays whose sum is divisible by 3 are: [3], [1, 4, 1], [3, 1, 4, 1].

Input: nums = [5, 10, -5, 20], k = 7

Output: 0

Explanation: There is no subarray whose sum is divisible by 7.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
2 <= k <= 104
"""

from collections import defaultdict

class Solution:
    def subarraySumDivisbleByK(self, nums, k):

        if not nums:
            return 0

        prefixMap = defaultdict(int)
        prefixMap[0] = 1

        current_sum = 0

        count = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            target = current_sum % k

            count += prefixMap[target]

            prefixMap[target] += 1

        return count



        
