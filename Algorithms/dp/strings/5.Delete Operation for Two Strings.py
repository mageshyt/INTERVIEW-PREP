"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4

"""

class Solution:
    # TOP DOWN
    def minDistance(self, word1: str, word2: str) -> int:
        dp={} # (idx1,idx2) -> min steps

        n,m=len(word1),len(word2)


        # Find LCS of word1 and word2

        def dfs(idx1,idx2):
            if idx1 < 0 or idx2 < 0:
                return 0

            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]

            # match

            if word1[idx1] == word2[idx2]:
                dp[(idx1,idx2)]=1+dfs(idx1-1,idx2-1)

            else:
                dp[(idx1,idx2)]=max(dfs(idx1-1,idx2),dfs(idx1,idx2-1))

            return dp[(idx1,idx2)]


        lcs=dfs(n-1,m-1)


        return (m+n-2*lcs)

    # BOTTOM UP
    def minDistance2(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)

        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        return (m+n-2*dp[n][m])


    # BOTTOM UP - SPACE OPTIMIZED

    def minDistance3(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)

        dp=[0 for _ in range(m+1)]

        for i in range(1,n+1):
            prev=0
            for j in range(1,m+1):
                temp=dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j]=1+prev
                else:
                    dp[j]=max(dp[j],dp[j-1])

                prev=temp

        return (m+n-2*dp[m])
    
s=Solution()

print(s.minDistance("sea","eat"))
print(s.minDistance("leetcode","etco"))

print("================================")
print(s.minDistance2("sea","eat"))
print(s.minDistance2("leetcode","etco"))


print("================================")
print(s.minDistance3("sea","eat"))
print(s.minDistance3("leetcode","etco"))
