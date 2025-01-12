"""
ou are given a string s and a pattern string p, where p contains exactly one '*' character.

The '*' in p can be replaced with any sequence of zero or more characters.

Return true if p can be made a substring of s, and false otherwise.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "leetcode", p = "ee*e"

Output: true

Explanation:

By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.

Example 2:

Input: s = "car", p = "c*v"

Output: false

Explanation:

There is no substring matching the pattern.

Example 3:

Input: s = "luck", p = "u*"

Output: true

Explanation:

The substrings "u", "uc", and "uck" match the pattern.

"""
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        splits= p.split('*')
        prefix, suffix = splits[0], splits[1]

        # # base case
        # if len(p) ==2:
        #     return prefix in s or suffix in s
        #
        for i in range(len(s) - len(prefix) + 1):
            print(s[i:i+len(prefix)])
            if s[i:i+len(prefix)] == prefix: # if prefix matches
                # find the suffix in the remaining string
                # no use of *
                if prefix + suffix in s:
                    return True

                # use of *
                for j in range(i+len(prefix), len(s)):
                    if s[j] == suffix[0]:
                        if s[j:j+len(suffix)] == suffix:
                            return True

        return False

        


# Test cases
print(Solution().hasMatch("leetcode", "ee*e"))  # Output: True
print(Solution().hasMatch("car", "c*v"))        # Output: False
print(Solution().hasMatch("luck", "u*"))        # Output: True

print(Solution().hasMatch("leetcode", "ee*"))   # Output: True
print(Solution().hasMatch("kvb", "k*v"))   # Output: True
