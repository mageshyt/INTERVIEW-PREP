from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n=len(s)
        res=[]

        def backtrack(i, path):
            if i==n:
                res.append(path)
                return

            # check if the character is a digit
            if s[i].isdigit():
                # if it is a digit, we just add it to the path
                backtrack(i+1, path+s[i])

            else:
            # decision: lowercase
                backtrack(i+1, path+s[i].lower())
            # decision: uppercase
                backtrack(i+1, path+s[i].upper())

        backtrack(0, "")
        return res

# Time complexity: O(2^n)
# Space complexity: O(n)
print("TESTING")
print(Solution().letterCasePermutation("a1b2"))
