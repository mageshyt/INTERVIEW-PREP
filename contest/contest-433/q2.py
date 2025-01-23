"""
You are given an integer array nums and a positive integer k. Return the sum of the maximum and minimum elements of all subsequences of nums with at most k elements.

A non-empty subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 24

Explanation:

The subsequences of nums with at most 2 elements are:

Subsequence	Minimum	Maximum	Sum
[1]	1	1	2
[2]	2	2	4
[3]	3	3	6
[1, 2]	1	2	3
[1, 3]	1	3	4
[2, 3]	2	3	5
Final Total	 	 	24
The output would be 24.

Example 2:

Input: nums = [5,0,6], k = 1

Output: 22

Explanation:

For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is 5 + 5 + 0 + 0 + 6 + 6 = 22.

Example 3:

Input: nums = [1,1,1], k = 2

Output: 12

Explanation:

The subsequences [1, 1] and [1] each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.©leetcode
"""

from typing import List

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        n=len(nums)
        nums.sort()

        dp={} # (idx,remaining) -> (min,max)

        def dfs(idx1,idx2):
            if idx2 == 0:
                return 1

            if idx1 == 0:
                return 0

            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]

            pick=dfs(idx1-1,idx2-1) # pick the current element
            not_pick=dfs(idx1-1,idx2) # not pick the current element

            dp[(idx1,idx2)]=(pick+not_pick)%mod

            return dp[(idx1,idx2)]
        result=0

        for i in range(n):
            for j in range(1,k+1):
                count_as_min=(dfs(i,j-1)*nums[i])%mod
                count_as_max=(dfs(n-i-1,j-1)*nums[i])%mod
                result=(result+count_as_max+count_as_min)%mod

        return result
    # SPACE OPTIMIZED
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        n=len(nums)
        nums.sort()

        dp=[[0] * (k+1) for _ in range(n+1)]
        dp[0][0]=1

        for i in range(1,n+1):
            dp[i][0]=1

            for j in range(1,min(i,k)+1):
                dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%mod

        result=0

        for i in range(n):
            for j in range(1,k+1):
                count_as_min=(dp[i][j-1]*nums[i])%mod
                count_as_max=(dp[n-i-1][j-1]*nums[i])%mod
                result=(result+count_as_max+count_as_min)%mod

        return result

s=Solution()
print(s.minMaxSums([1,2,3],2)) # 24
print(s.minMaxSums([5,0,6],1)) # 22
print(s.minMaxSums([1,1,1],2)) # 12
