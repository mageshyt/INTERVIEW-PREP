"""

Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.


Examples:
Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3

Output: True

Explanation: The element 3 is present in the array. So, the answer is True.

Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10

Output: False

Explanation:The element 10 is not present in the array. So, the answer is False.

Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 7

Output:
1
Constraints:
  1 <= nums.length <= 104
  -104 <= nums[i] <= 104
  nums is guaranteed to be rotated at some pivot.
  -104 <= k <= 104

"""

class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):

        low,high=0,len(nums)-1

        while low <= high:
            mid=(low+high)//2

            if nums[mid]==k:
                return True
            # special case

            if nums[mid] == nums[low] == nums[high]:
                low+=1
                high-=1
                continue

            elif nums[mid] >= nums[low] :

                if k>= nums[low] and nums[mid] > k :
                    high=mid-1
                else:
                    low=mid+1

            else:
                if k > nums[mid] and k <=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return False



