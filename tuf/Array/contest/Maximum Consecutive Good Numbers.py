"""
Given an array of integers nums and an array goodNumbers, return the maximum number of consecutive good numbers in the array.



Any number present in the goodNumbers array is a good number.


Examples:
Input: nums = [1, 2, 3, 5, 4, 5, 1], goodNumbers = [3, 5]

Output: 2

Explanation: [1, 2, 3, 5, 4, 5, 1] the underlined numbers are all good numbers and give the maximum length.

Input: nums = [4, 8, 1, 2, 0, 4, 6], goodNumbers = [1, 4, 2, 6]

Output: 2

Explanation: [4, 8, 1, 2, 0, 4, 6] the underlined numbers are all good numbers and give the maximum length.

Note that the segment with index [6, 7] was also a possible answer.

Constraints:
1 <= nums.length <= 105
1 <= goodNumbers.length <= 105
-104 <= nums[i], goodNumbers[i] <= 104

"""

class Solution:
    def maxConsecutiveGoodNums(self, nums, goodNumbers):
        goodset = set(goodNumbers)
        max_consec = 0
        current_consec = 0
        
        for num in nums:
            if num in goodset:
                current_consec += 1
                max_consec = max(max_consec, current_consec)
            else:
                current_consec = 0
                
        return max_consec

# Time complexity: O(n)
# Space complexity: O(n)
