"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

"""

class Solution:
    # TOP DOWN
    # Time : O(n*m) | Space : O(n*m) + O(n)
    def isMatch(self, s: str, p: str) -> bool:
        dp={} # 
        n,m=len(s),len(p)


        def dfs(idx1,idx2):

            if idx2 < 0:
                return idx1 < 0

            if idx1 < 0:
                return all([c=="*" for c in p[:idx2+1]])

            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]

            if s[idx1] == p[idx2] or p[idx2]=="?":
                dp[(idx1,idx2)]=dfs(idx1-1,idx2-1)

            elif p[idx2]=="*":

                # * can match 0 or more characters

                dp[(idx1,idx2)]=dfs(idx1-1,idx2) or dfs(idx1,idx2-1)
            else:
                dp[(idx1,idx2)]=False

            return dp[(idx1,idx2)]


        return dfs(n-1,m-1)

    # BOTTOM UP
    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)

        dp=[[False]*(m+1) for _ in range(n+1)]

        dp[0][0]=True # empty string matches empty pattern

        # fill the base case
        for i in range(1,m+1):
            if p[i-1]=="*":
                dp[0][i]=dp[0][i-1]


        for i in range(1,n+1):
            for j in range(1,m+1):

                if s[i-1]==p[j-1] or p[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]

                elif p[j-1]=="*":
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]

        return dp[n][m]

    # BOTTOM UP OPTIMIZED

    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)
        prev=[False]*(m+1)
        prev[0]=True

        for i in range(1,m+1):
            if p[i-1]=="*":
                prev[i]=prev[i-1]

        for i in range(1,n+1):
            curr=[False]*(m+1)
            for j in range(1,m+1):

                if s[i-1]==p[j-1] or p[j-1]=="?":
                    curr[j]=prev[j-1]

                elif p[j-1]=="*":
                    curr[j]=prev[j] or curr[j-1]

            prev=curr

        return prev[m]


    

s=Solution()
print(s.isMatch("abcabczzzde","*abc???de*")) # False

