"""Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""
from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap=defaultdict(int)

        for num in nums:
            hMap[num]+=1

        return [key for key, value in sorted(hMap.items(),key=lambda x:x[1],reverse=True)][:k]

print(Solution().topKFrequent([1,2,2,3,3,3], 2)) # [2,3]
print(Solution().topKFrequent([7,7], 1)) # [7]
