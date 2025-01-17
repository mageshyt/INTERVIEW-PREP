from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1] * n
        hash={}
        maxi=1

        idx=0

        for i in range(n):
            hash[i]=i

            for prev in range(0,i):
                if nums[prev] < nums[i] and dp[i] < dp[prev]+1:
                    dp[i]=dp[prev]+1
                    hash[i]=prev

            if dp[i] > maxi:
                maxi=dp[i]
                idx=i

        res=[]

        while hash[idx] != idx:
            res.append(nums[idx])
            idx=hash[idx]

        res.append(nums[idx])

        print("LIST: ",res[::-1]) 

        return maxi


s=Solution()

print(
    s.lengthOfLIS([10,9,2,5,3,7,101,18]) # 4
)
 
