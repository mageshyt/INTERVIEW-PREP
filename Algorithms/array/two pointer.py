# 125. valid palindrome

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s=s.lower()
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().isPalindrome("A man, a plan, a canal: Panama")) # True
print(Solution().isPalindrome("race a car")) # False

# 167. Two Sum II - Input Array Is Sorted

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            # if sum of left and write is greater than target means we have to move right so that our sum will decreasing

            if nums[l]+ nums[r] > target:
                r -= 1

            elif nums[l]+ nums[r] < target:
            # if sum of left and write is less than target means we have to move left so that our sum will increase
                l += 1

            else:
                return [l+1, r+1]
        return [0,0]
# Time complexity: O(n)
# Space complexity: O(1)
print(Solution().twoSum([2,7,11,15], 9)) # [1,2]


# 11. Container With Most Water

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        l, r = 0, len(height) - 1
        while l < r :
            minH = min(height[l], height[r])
            width = r - l

            maxArea = max(maxArea, minH * width)

            # now lets increate the height of the container 

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1


        return maxArea

# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
