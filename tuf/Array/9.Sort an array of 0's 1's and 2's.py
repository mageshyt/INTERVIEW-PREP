"""
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.


Examples:
Input: nums = [1, 0, 2, 1, 0]

Output: [0, 0, 1, 1, 2]

Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Input: nums = [0, 0, 1, 1, 1]

Output: [0, 0, 1, 1, 1]

Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos

Input: nums = [1, 1, 2, 2, 1]

Output:
[1, 1, 1, 2, 2]

"""
class Solution:
    def sortZeroOneTwo(self, nums):
        # 3 pointers: low, mid, high
        low, mid, high = 0, 0, len(nums) - 1

        while low <=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


        return nums

