"""
You are given an array of integers nums and an integer target.

For each number in the array, you can choose to either add or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.

Example 1:

Input: nums = [2,2,2], target = 2

Output: 3
Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
+2 +2 -2 = 2
+2 -2 +2 = 2
-2 +2 +2 = 2
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={} # (index,target) -> count

        def dfs(index,target):
            if index == len(nums):
                return 1 if target == 0 else 0

            if (index,target) in dp:
                return dp[(index,target)]

            count=0
            count += dfs(index+1,target-nums[index]) # ADD
            count += dfs(index+1,target+nums[index]) # SUBTRACT

            dp[(index,target)]=count


            return dp[(index,target)]

        return dfs(0,target)


    # Better solution

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass
    


# Time : O(N*M) | Space : O(N*M)
print(Solution().findTargetSumWays([2,2,2],2)) # 3

