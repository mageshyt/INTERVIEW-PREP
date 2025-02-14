"""

Given an array nums of n integers, return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.


Examples:
Input: nums = [100, 4, 200, 1, 3, 2]

Output: 4

Explanation: The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.

Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Output: 9

Explanation: The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9. 

Input: nums = [1, 9, 3, 10, 4, 20, 2]

Output:
2
"""


class Solution:
    # Time complexity: O(NlogN) | Space complexity: O(1)
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums.sort()
        longest, cnt = 1, 1
        prev = nums[0]
        
        for num in nums[1:]:
            if num == prev:
                # Skip duplicates.
                continue
            elif num - 1 == prev:
                cnt += 1
            else:
                cnt = 1
            prev = num
            longest = max(longest, cnt)
        
        return longest

    # Time complexity: O(N) | Space complexity: O(N)
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # check if the current number is the start of a sequence.
            if num - 1 not in num_set:
                current_num = num
                next_num = num + 1
                current_streak = 1
                
                while next_num in num_set:
                    current_num += 1
                    next_num += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)

        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
