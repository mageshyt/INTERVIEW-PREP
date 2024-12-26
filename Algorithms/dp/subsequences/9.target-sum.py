
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={} # (index,target) -> count

        total=sum(nums)

        if total - target < 0 or (total - target) % 2 != 0:
            return 0


        newTarget=(total-target)//2

        def dfs(idx,target):
            if  idx ==0:
                # case 1 : target == 0  or nums[0] == 0
                if target == 0 or target == nums[0]:
                    return 1

                if target ==0 and nums[0] ==0:
                    return 2 

                return 0

            if (idx,target) in dp:
                return dp[(idx,target)]


            take=0
            if nums[idx] <= target:
                take=dfs(idx-1,target-nums[idx])

            notTake=dfs(idx-1,target)


            dp[(idx,target)]=take+notTake


            return dp[(idx,target)]



        return dfs(len(nums)-1,newTarget)
s=Solution()

print(s.findTargetSumWays([2,2,2],2)) # 3

 

                

            


