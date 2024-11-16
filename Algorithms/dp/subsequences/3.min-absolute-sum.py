"""
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

 

Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
"""

from typing import List
class Solution:

    def minimumDifference(self, nums: List[int]) -> int:
        # ignore the negative sign
        nums = [abs(num) for num in nums]
        total=sum(nums)
        n=len(nums)

        # Find the subset sum of all possible subsets for s1

        dp=[False] * (total+1)
        if nums[0] <= total:
            dp[nums[0]] = True

        for i in range(1,n):
            for target in range(1,total+1):
                take=False
                notTake= dp[target]
                if nums[i] <= target:
                    take = dp[target-nums[i]]
                dp[target] = take or notTake

        # Find the minimum difference between s1 and s2
        res=float('inf')

        for i in range(total//2+1): # iterate till half of the total sum
            if dp[i]:
                res = min(res,total-2*i)

        return res

print(Solution().minimumDifference([2,3,7])) # 0
        
