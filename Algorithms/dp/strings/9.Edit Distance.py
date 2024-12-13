"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={} # (idx1,idx2) -> min steps

        n,m=len(word1),len(word2)

        def dfs(idx1,idx2):
            if idx2 < 0:
                return idx1+1


            if idx1 < 0:
                return idx2+1

            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]


            # match

            if word1[idx1] == word2[idx2]:
                dp[(idx1,idx2)]=dfs(idx1-1,idx2-1)

            else:
                insert=1+dfs(idx1,idx2-1)
                delete=1+dfs(idx1-1,idx2)
                replace=1+dfs(idx1-1,idx2-1)

                dp[(idx1,idx2)]=min(insert,delete,replace)


            return dp[(idx1,idx2)]



        return dfs(n-1,m-1)

    # BOTTOM UP

    def minDistance2(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        # fill the base case

        for i in range(n+1):
            dp[i][0]=i

        for j in range(m+1):
            dp[0][j]=j

        for i in range(1,n+1):
            for j in range(1,m+1):

                if word1[i-1] == word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]

                else:
                    insert=1+dp[i][j-1]
                    delete=1+dp[i-1][j]
                    replace=1+dp[i-1][j-1]

                    dp[i][j]=min(insert,delete,replace)


        return dp[n][m]







s=Solution()
print(s.minDistance("horse","ros"))
print(s.minDistance("intention","execution"))

print("===============")

print(s.minDistance2("horse","ros"))
print(s.minDistance2("intention","execution"))
