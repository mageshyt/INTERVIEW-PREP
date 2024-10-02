"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

"""
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        res=0

        def isUnique(s):
            return len(s)==len(set(s))

        def backTrack(idx,path):
            nonlocal res
            res = max(res,len(path))
            # base case if we reach the end of the array
            if idx >= n:
                return

            for i in range(idx,n):
                if isUnique(path+arr[i]):
                    backTrack(i+1,path+arr[i])

        backTrack(0,'')

        return res




# Time complexity: O(2^n)
# Space complexity: O(2^n)

print(Solution().maxLength(["un","iq","ue"])) # 4
print(Solution().maxLength(["cha","r","act","ers"])) # 6
