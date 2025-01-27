from typing import List
class Solution:
    # Function to move zeroes to the end
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        right = 0

        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


s=Solution()

nums = [0,1,0,3,12]
s.moveZeroes(nums)

print(nums) # [1, 3, 12, 0, 0]


