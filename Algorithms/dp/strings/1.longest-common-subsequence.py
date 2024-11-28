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




s=Solution()

print("===========BRUTE FORCE SOLUTION============")
print(s.lcs("abc", "abc")) # 3

print("===========TOP DOWN MEMOIZATION============")
print(s.longestCommonSubsequence("abc", "def")) # 0
print(s.longestCommonSubsequence("abcde", "ace")) # 3
