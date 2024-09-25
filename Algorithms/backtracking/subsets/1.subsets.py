"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

from typing import List

class solution:
    def subsets(self,nums):
        subsets,curset= [],[]
        self.helper(nums,0,curset,subsets) # array, index, path, result
        return subsets 
    def helper(self,nums:List[int],i:int,path:List[int],subsets:List[List[int]]):
        if i == len(nums):
            subsets.append(path.copy())
            return
        # decision: pick the number
        path.append(nums[i])
        self.helper(nums,i+1,path,subsets)
        path.pop()

        # decision: not pick the number
        self.helper(nums,i+1,path,subsets)

# Time complexity: O(2^n*n)
# Space complexity: O(n)

print("TEST CASES")
print(solution().subsets([1,2,2])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(solution().subsets([0])) # [[],[0]]

        
