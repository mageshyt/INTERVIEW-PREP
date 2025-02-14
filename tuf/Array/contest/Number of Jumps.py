"""
Given an array nums of n integers and an integer k, return the total number of jumps needed in the array.



An element nums[i] needs to jump another element nums[j] if:

0 <= i < j <= n-1
nums[i] + k < nums[j]

Examples:
Input: nums = [3, 1, 10, 6, 5], k = 2

Output: 5

Explanation: Number of jumps for each index:

nums[0] -> 2, nums[1] -> 3, nums[2] -> 0, nums[3] -> 0, nums[4] -> 0

Total = 2 + 3 + 0 + 0 + 0 = 5

Input: nums = [1, 4, 5, 1, 7], k = 3

Output: 3

Explanation: Number of jumps for each index:

nums[0] -> 2, nums[1] -> 0, nums[2] -> 0, nums[3] -> 1, nums[4] -> 0

Total = 2 + 0 + 0 + 1 + 0 = 3

Constraints:
1 <= n <= 105
-104 <= nums[i] <= 104
0 <= k <= 104

"""

from typing import List

class Solution:
    def NumberOfJumps(self, nums: List[int], k: int) -> int:

        def merge_sort(arr: List[int]) -> (List[int], int):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, count_left = merge_sort(arr[:mid]) # (sorted left half, number of jumps in left half)
            right, count_right = merge_sort(arr[mid:]) # (sorted right half, number of jumps in right half)
            
            count = count_left + count_right
            j = 0
            # Count valid cross pairs: for each x in left, count how many y in right satisfy y > x + k.
            for x in left:
                while j < len(right) and right[j] <= x + k:
                    j += 1
                count += len(right) - j
            
            # Merge the two sorted lists.
            merged = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, count

        # Call the merge sort helper on the original array.
        _, total = merge_sort(nums)
        return total
