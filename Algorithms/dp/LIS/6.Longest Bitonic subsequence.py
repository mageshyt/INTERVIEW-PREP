
from typing import List

class Solution:
    def LongestBitonicSequence(self,n, nums: List[int]) -> int:
        dp1=[1] * n

        for i in range(n):
            for prev in range(0,i):
                if nums[prev] < nums[i]:
                    dp1[i]=max(dp1[prev]+1,dp1[i])

        dp2=[1] * n

        for i in range(n-1,-1,-1):
            for prev in range(n-1,i,-1):
                if nums[prev] < nums[i] :
                    dp2[i]=max(dp2[prev]+1,dp2[i])

        maxi=-1

        for i in range(n):
            maxi=max(maxi,dp1[i]+dp2[i]-1)

        return maxi


s=Solution()
print(s.LongestBitonicSequence(8,[1,11,2,10,4,5,2,1])) # 6
print(s.LongestBitonicSequence(3,[5,7,9]))
