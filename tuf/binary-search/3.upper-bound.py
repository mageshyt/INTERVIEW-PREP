"""
Given a sorted array of nums and an integer x, write a program to find the upper bound of x. The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than a given key i.e. x.

If no such index is found, return the size of the array.


Examples:
Input : n= 4, nums = [1,2,2,3], x = 2

Output:3

Explanation: Index 3 is the smallest index such that arr[3] > x.

Input : n = 5, nums = [3,5,8,15,19], x = 9

Output: 3

Explanation: Index 3 is the smallest index such that arr[3] > x.
"""


class Solution:
    def upperBound(self,nums,x):
        low,high=0,len(nums)-1

        while low <= high:
            mid=(low+high) // 2

            if nums[mid] <= x:
                low=mid+1
            else:
                high=mid-1

        return low if low < len(nums) else len(nums)
