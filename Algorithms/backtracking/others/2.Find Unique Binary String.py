"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

"""
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)

        def backTrack(idx,path):
            if idx == len(nums[0]):
                return None if path in s else path 

            # decision : pick 0
            res = backTrack(idx+1,path+'0')
            if res:
                return res

            # decision : pick 1

            res = backTrack(idx+1,path+'1')
            if res:
                return res

            return None

        return backTrack(0,'')

# Time complexity: O(2^n)
# Space complexity: O(2^n)
print(Solution().findDifferentBinaryString(["01","10"])) # "11"
print(Solution().findDifferentBinaryString(["00","01"])) # "11"
print(Solution().findDifferentBinaryString(["111","011","001"])) # "101"

