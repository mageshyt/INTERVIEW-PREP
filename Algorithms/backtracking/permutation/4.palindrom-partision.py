from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end]) # add the substring to the path
                    backtrack(end, path) 
                    path.pop() # backtrack
        
        res = []
        backtrack(0, [])
        return res

# Time complexity: O(n*2^n)
# Space complexity: O(n)
print(Solution().partition("aab")) # [["a","a","b"],["aa","b"]]


