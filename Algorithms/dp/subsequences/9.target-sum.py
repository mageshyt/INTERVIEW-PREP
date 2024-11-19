
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={} # (index,target) -> count

        def dfs(idx,target):
            if idx == 0:
                return 1 if target == 0 else 0

            if (idx,target) in dp:
                return dp[(idx,target)]


            add=dfs(idx-1,target-nums[idx]) # ADD
            subtract=dfs(idx-1,target+nums[idx])

            dp[(idx,target)]=add+subtract

            return dp[(idx,target)]


        return dfs(len(nums)-1,target)

    # BOTTOM UP

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=[[0]*(target+1) for _ in range(len(nums))]

        # FILL BASE CASE

        pass

