"""
You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].©leetcode
"""

from typing import List
import bisect

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        nums.sort()

        arr=[nums[0]-k]


        for n in nums[1:]:
            search=range(n-k,n+k+1)

            x=bisect.bisect_left(search,arr[-1]+1)

            if x==len(search):
                continue

            arr.append(search[x])

        return len(arr)


print(Solution().maxDistinctElements([1,2,2,3,3,4],2)) #6
print(Solution().maxDistinctElements([4,4,4,4],1)) #3
