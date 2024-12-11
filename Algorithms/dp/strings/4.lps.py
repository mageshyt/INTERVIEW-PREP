"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1,s2=s,s[::-1]

        prev=[0]*(len(s2)+1)
        curr=[0]*(len(s2)+1)

        for i in range(1,len(s1)+1):
            for j in range(1,len(s)+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])

            prev=curr.copy()

        return curr[-1]

    def PrintlongestPalindromeSubseq(self, s: str) -> int:
        s1,s2=s,s[::-1]

        n,m=len(s1),len(s2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        res=[0]*dp[n][m]

        i,j=n,m

        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                res[dp[i][j]-1] = s1[i-1]
                i,j=i-1,j-1
            elif dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1

        return "".join(res)
       
    


    
s=Solution()
print(s.longestPalindromeSubseq("bbbab"))
print(s.longestPalindromeSubseq("cbbd"))
print(s.PrintlongestPalindromeSubseq("bbbab"))
print(s.PrintlongestPalindromeSubseq("cbbd"))
