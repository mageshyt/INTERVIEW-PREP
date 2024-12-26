"""
You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.

An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

Note that special numbers, the sum element, and the outlier must have distinct indices, but may share the same value.

Return the largest potential outlier in nums.

 

Example 1:

Input: nums = [2,3,5,10]

Output: 10

Explanation:

The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.
"""

from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n=len(nums)
        freq=Counter(nums)
        total=sum(nums)

        maxOutlier=float('-inf')

        for num in nums:
            requiredSum=total-num

            if requiredSum %2 != 0:
                continue

            requiredSum //= 2

            freq[num] -= 1

            if freq[requiredSum] > 0:
                maxOutlier=max(maxOutlier,num)

            freq[num] += 1

        return maxOutlier

nums=[9,-6,9]

s=Solution()
print(s.getLargestOutlier(nums))
print(s.getLargestOutlier([2,3,5,10]))
print(s.getLargestOutlier([-310,-720,-720]))
print(s.getLargestOutlier([1,1,1,1,1,5,5]))




# Time complexity O(nlogn) | Space complexity O(1)

