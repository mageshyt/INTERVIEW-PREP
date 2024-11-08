"""
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.


"""

class Solution:
    def checkString(self, s: str) -> bool:
        isB = False
        for char in s:
            if char == 'b':
                isB = True

            if isB and char == 'a':
                return False

        return True
print(Solution().checkString("ab")) #True
print(Solution().checkString("abab")) #False
