"""
You are given a 0-indexed integer array nums having length n, and an integer k.

You can perform the following increment operation any number of times (including zero):

Choose an index i in the range [0, n - 1], and increase nums[i] by 1.
An array is considered beautiful if, for any subarray with a size of 3 or more, its maximum element is greater than or equal to k.

Return an integer denoting the minimum number of increment operations needed to make nums beautiful.

A subarray is a contiguous non-empty sequence of elements within an array

Example 1:

Input: nums = [2,3,0,0,2], k = 4
Output: 3
Explanation: We can perform the following increment operations to make nums beautiful:
Choose index i = 1 and increase nums[1] by 1 -> [2,4,0,0,2].
Choose index i = 4 and increase nums[4] by 1 -> [2,4,0,0,3].
Choose index i = 4 and increase nums[4] by 1 -> [2,4,0,0,4].
The subarrays with a size of 3 or more are: [2,4,0], [4,0,0], [0,0,4], [2,4,0,0], [4,0,0,4], [2,4,0,0,4].
In all the subarrays, the maximum element is equal to k = 4, so nums is now beautiful.
It can be shown that nums cannot be made beautiful with fewer than 3 increment operations.
Hence, the answer is 3.
Example 2:

Input: nums = [0,1,3,3], k = 5
Output: 2
Explanation: We can perform the following increment operations to make nums beautiful:
Choose index i = 2 and increase nums[2] by 1 -> [0,1,4,3].
Choose index i = 2 and increase nums[2] by 1 -> [0,1,5,3].
The subarrays with a size of 3 or more are: [0,1,5], [1,5,3], [0,1,5,3].
In all the subarrays, the maximum element is equal to k = 5, so nums is now beautiful.
It can be shown that nums cannot be made beautiful with fewer than 2 increment operations.
Hence, the answer is 2.
Example 3:

Input: nums = [1,1,2], k = 1
Output: 0
Explanation: The only subarray with a size of 3 or more in this example is [1,1,2].
The maximum element, 2, is already greater than k = 1, so we don't need any increment operation.
Hence, the answer is 0.
"""

from typing import List

class Solution:
    # Top Down
    # Time : O(n) | Space : O(n) + O(n) = O(n)
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp={} # (idx)-> min operations

        n=len(nums)

        def dfs(idx):
            if idx in dp:
                return dp[idx]

            if idx < 0:
                return 0


            way1=max(0,k-nums[idx]) + dfs(idx-1)
            way2=max(0,k-nums[idx-1]) + dfs(idx-2) if idx-1>=0 else 0
            way3=max(0,k-nums[idx-2]) + dfs(idx-3) if idx-2>=0 else 0

            dp[idx]=min(way1,way2,way3)

            return dp[idx]

        return dfs(n-1)


    # Bottom Up

    # Time : O(n) | Space : O(n)

    def minIncrementOperations2(self, nums: List[int], k: int) -> int:
        dp=[0]*len(nums)

        for i in range(2,len(nums)):
            way1=max(0,k-nums[i]) + dp[i-1] 
            way2=max(0,k-nums[i-1]) + dp[i-2] if i-1>=0 else 0
            way3=max(0,k-nums[i-2]) + dp[i-3] if i-2>=0 else  0

            dp[i]=min(way1,way2,way3)

        return dp[-1]

    # Bottom Up with space optimization
    # Time : O(n) | Space : O(1)

    def minIncrementOperations3(self, nums: List[int], k: int) -> int:
        dp=[0]*3
        cur=[0]*3

        for i in range(2,len(nums)):
            way1=max(0,k-nums[i]) + dp[2] 
            way2=max(0,k-nums[i-1]) + dp[1] if i-1>=0 else 0
            way3=max(0,k-nums[i-2]) + dp[0] if i-2>=0 else  0

            cur[2]=min(way1,way2,way3)
            dp=cur



        return dp[-1]


s=Solution()
print(s.minIncrementOperations([2,3,0,0,2],4)) # 3
print(s.minIncrementOperations([0,1,3,3],5)) # 2
print(s.minIncrementOperations([1,1,2],1)) # 0
print(s.minIncrementOperations([0,5,5],8)) # 3

print("Bottom Up")

print(s.minIncrementOperations2([2,3,0,0,2],4)) # 3
print(s.minIncrementOperations2([0,1,3,3],5)) # 2
print(s.minIncrementOperations2([1,1,2],1)) # 0
print(s.minIncrementOperations2([0,5,5],8)) # 0

print("Bottom Up with space optimization")

print(s.minIncrementOperations3([2,3,0,0,2],4)) # 3
print(s.minIncrementOperations3([0,1,3,3],5)) # 2
print(s.minIncrementOperations3([1,1,2],1)) # 0
print(s.minIncrementOperations3([0,5,5],8)) # 0




