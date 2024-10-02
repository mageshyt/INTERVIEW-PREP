"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.helper(n,n,"",res)

        return res

    def helper(self,left,right,curr,res):
        # base case
        if left==0 and right==0:
            res.append(curr)
            return

        # decision: pick the left generateParenthesis
        if left>0:
            self.helper(left-1,right,curr+"(",res)

        # decision: pick the right generateParenthesis
        if right>left:
            self.helper(left,right-1,curr+")",res)


    


# Time complexity: O(4^n/sqrt(n))
# Space complexity: O(4^n/sqrt(n))
print("TEST CASES")
print(Solution().generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]

