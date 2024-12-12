"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        s1,s2=s,s[::-1]

        n,m=len(s1),len(s2)

        prev=[0]*(n+1)
        curr=[0]*(n+1)

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])

            prev=curr.copy()



        return (n-curr[-1])
s=Solution()

print(s.minInsertions("zzazz"))
print(s.minInsertions("mbadm"))
print(s.minInsertions("leetcode"))
