"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

"""
class Solution:
    # TOP DOWN
    # Time complexity : O(n*m) | Space complexity : O(n*m) + O(n)
    def numDistinct(self, s: str, t: str) -> int:
        dp={} # (i,j) -> number of distinct subsequences

        n,m=len(s),len(t)

        def dfs(i,j):
            # if we have reached end of t

            if j < 0:
                return 1

            # if we have reached end of s but not t
            if i < 0: 
                return 0

            if (i,j) in dp:
                return dp[(i,j)]


            # if characters match
            if s[i] == t[j]:
                take=dfs(i-1,j-1)
                skip=dfs(i-1,j)

                dp[(i,j)]=take+skip

            else:
                dp[(i,j)]=dfs(i-1,j)


            return dp[(i,j)]


        return dfs(n-1,m-1)

    # BOTTOM UP
    # Time complexity : O(n*m) | Space complexity : O(n*m)

    def numDistinct2(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][m]

    # BOTTOM UP - SPACE OPTIMIZED
    # Time complexity : O(n*m) | Space complexity : O(m)
    def numDistinct3(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        prev=[0]*(m+1)

        prev[0]=1

        for i in range(1,n+1):

            for j in range(m,0,-1):
                if s[i-1] == t[j-1]:
                    prev[j]=prev[j-1]+prev[j]
                else:
                    prev[j]=prev[j]


        return prev[m]

                


print(Solution().numDistinct3("rabbbit","rabbit"))
print(Solution().numDistinct3("babgbag","bag"))
