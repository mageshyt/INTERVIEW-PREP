"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""
from collections import defaultdict
import collections 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) != len(t):
             return False

        hMap = defaultdict(int)

        for char in s:
            hMap[char] += 1

        for char in t:
            # if char not in hMap return False
            if char not in hMap:
                return False

            elif hMap[char] == 0:
                return False
            else:
                hMap[char] -= 1

        return True

        
print(Solution().isAnagram("anagram", "nagaram")) # True
print(Solution().isAnagram("rat", "car")) # false
print(Solution().isAnagram("a", "ab")) # false

    

    

