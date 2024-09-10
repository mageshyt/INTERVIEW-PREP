

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hMap:
                return [hMap[diff], i]
            hMap[num] = i

        return []
print(Solution().twoSum([2,7,11,15], 9)) # [2, 7]
print(Solution().twoSum([3,2,4], 6)) # [2, 4]

