"""Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n,m=len(str1),len(str2)

        dp= [[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]== str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        i,j=n,m

        res=""

        while i > 0 and j > 0:

            # if both characters are same
            if str1[i-1] == str2[j-1]:
                res+=str1[i-1]
                i-=1
                j-=1

            elif dp[i-1][j] > dp[i][j-1]:
                # move : up
                res+=str1[i-1]
                i-=1
            else:
                # move : left
                res+=str2[j-1]
                j-=1


        # if there are remaining characters in str1 or str2
        while i > 0:
            res+=str1[i-1]
            i-=1

        while j > 0:
            res+=str2[j-1]
            j-=1


        return res[::-1]

s=Solution()

print(s.shortestCommonSupersequence("abac","cab")) # "cabac"
