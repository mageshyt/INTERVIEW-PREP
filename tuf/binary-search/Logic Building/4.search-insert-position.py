"""
Given a sorted array of nums consisting of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


Examples:
Input: nums = [1, 3, 5, 6], target = 5

Output: 2

Explanation: The target value 5 is found at index 2 in the sorted array. Hence, the function returns 2.

Input: nums = [1, 3, 5, 6], target = 2

Output: 1

Explanation: The target value 2 is not found in the array. However, it should be inserted at index 1 to maintain the sorted order of the array.
"""


class Solution:
    def searchInsert(self, nums, target):
        low,high=0,len(nums)-1

        while low <= high:

            mid=(low+high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low=mid+1

            else:
                high=mid-1
        return low


print("TEST CASES")

s=Solution()

print(s.searchInsert([1, 3, 5, 6],5)) # 2

print(s.searchInsert([1, 3, 5, 6],2)) # 1

print(s.searchInsert([1, 3, 5, 6],7)) # 4

