"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1].


Examples:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8

Output: [3, 4]

Explanation:The target is 8, and it appears in the array at indices 3 and 4, so the output is [3,4]

Input: nums = [5, 7, 7, 8, 8, 10], target = 6

Output: [-1, -1]

Expalantion: The target is 6, which is not present in the array. Therefore, the output is [-1, -1].
"""

class Solution:
    def searchRange(self, nums, target):

        first=self.findFirstOccurrence(nums,target)
        last=self.findLastOccurrence(nums,target)

        return [first,last]

    def findFirstOccurrence(self, nums, target):
        low,high=0,len(nums)-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                if mid==0 or nums[mid-1]!=target:
                    return mid
                else:
                    high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1

        return -1


    def findLastOccurrence(self, nums, target):
        low,high=0,len(nums)-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                if mid==len(nums)-1 or nums[mid+1]!=target:
                    return mid
                else:
                    low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1

        return -1


s=Solution()

print(s.searchRange([5, 7, 7, 8, 8, 10],8))
print(s.searchRange([5, 7, 7, 8, 8, 10],6))
