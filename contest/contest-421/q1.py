from math import lcm,gcd
from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n=len(nums)
        max_score=lcm(*nums) * gcd(*nums)
        if n==1:
            return nums[0]*nums[0]

        for i in range(n):
            #find the gcd of all the nums except i
            gcd_except_i=gcd(*nums[:i]+nums[i+1:])
            lcm_except_i=lcm(*nums[:i]+nums[i+1:])
            print(gcd_except_i,lcm_except_i)
            max_score=max(max_score,lcm_except_i*gcd_except_i)

        return max_score
print(Solution().maxScore([6,14,20])) # 10

