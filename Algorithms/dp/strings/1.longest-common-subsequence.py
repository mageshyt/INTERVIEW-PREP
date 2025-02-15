"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""


class Solution:
    # BRUTE FORCE SOLUTION

    # Time: O(2^n) | Space: O(n)
    def lcs(self,s1, s2):
        # find all subsequences of s1
        def subsequences(idx,path,subset):
            if idx == len(s1):
                subset.append(path)
                return
            # decision: pick the element
            subsequences(idx+1,path+s1[idx],subset)
            # decision: not pick the element
            subsequences(idx+1,path,subset)

        s1_subseq = []
        s2_subseq = []

        subsequences(0,"",s1_subseq)
        subsequences(0,"",s2_subseq)


        # find the longest common subsequence

        for i in range(len(s1_subseq)):
            for j in range(len(s2_subseq)):
                if s1_subseq[i] == s2_subseq[j]:
                    return len(s1_subseq[i])

        return 0

    # TOP DOWN MEMOIZATION
    # Time: O(n*m) | Space: O(n*m) + O(n) + O(m)
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp={}

        def dfs(idx1,idx2):
            if idx1 < 0 or idx2 < 0:
                return 0

            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]

            # case : match

            if s1[idx1] == s2[idx2]:
                return 1 + dfs(idx1-1,idx2-1)

            # case: not match
            not_match = max(dfs(idx1-1,idx2),dfs(idx1,idx2-1))

            dp[(idx1,idx2)] = not_match

            return not_match

        return dfs(len(s1)-1,len(s2)-1)

    # BOTTOM UP TABULATION
    # Time: O(n*m) | Space: O(n*m)

    def longestCommonSubsequence2(self, s1: str, s2: str) -> int:
        n,m=len(s1),len(s2)
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1,n+1):  
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])


  
        return dp[n][m]

    # SPACE OPTIMIZED BOTTOM UP TABULATION
    # Time: O(n*m) | Space: O(m)
    def longestCommonSubsequence3(self, s1: str, s2: str) -> int:
        n,m=len(s1),len(s2)
        prev=[0 for _ in range(m+1)]
        curr=[0 for _ in range(m+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j]=max(prev[j],curr[j-1])

            prev=curr.copy()

        return prev[m]




s=Solution()

print("===========BRUTE FORCE SOLUTION============")
print(s.lcs("abc", "abc")) # 3

print("===========TOP DOWN MEMOIZATION============")
print(s.longestCommonSubsequence("abc", "def")) # 0
print(s.longestCommonSubsequence("abcde", "ace")) # 3

print("===========BOTTOM UP ============")
print(s.longestCommonSubsequence2("abc", "def")) # 0
print(s.longestCommonSubsequence2("abcde", "ace")) # 3
