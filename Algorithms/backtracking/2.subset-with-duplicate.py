"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets,curset= [],[]
        nums.sort()
        self.helper(nums,0,curset,subsets)
        return subsets

    def helper(self,nums:List[int],i:int,curset:List[int],subsets:List[List[int]]):
        # base case
        if i == len(nums):
            subsets.append(curset.copy())
            return

        # decision: pick the number
        curset.append(nums[i])
        self.helper(nums,i+1,curset,subsets)

        # backtrack the decision

        curset.pop()

        # decision: not pick the number and skip the duplicates

        while i+1 < len(nums) and nums[i]==nums[i+1]:
            i+=1

        self.helper(nums,i+1,curset,subsets)

# Time complexity: O(2^n*n)
# Space complexity: O(n)

print("TEST CASES")
print(Solution().subsetsWithDup([1,2,2])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


