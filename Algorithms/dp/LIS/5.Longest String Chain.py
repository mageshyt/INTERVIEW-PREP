"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


""" 
from typing import List
from collections import Counter
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        maxi=0
        dp=[1] * len(words)

        words.sort(key=lambda x:len(x))
        for i in range(len(words)):
            for j in range(0,i):

                if self.compare(words[i],words[j]) and dp[i] <  dp[j]+1:
                    dp[i]=1+dp[j]

                maxi=max(dp[i],maxi)

        return maxi

    def compare(self,str1,str2):
        # at max it can have only 1 difference
        if len(str1) != len(str2) + 1: 
            return False

        l1,l2=0,0

        while l1 < len(str1):
            if l2 < len(str2) and str1[l1] == str2[l2]:
                l1+=1
                l2+=1
            else:
                l1+=1
        

        if (l1 == len(str1) and l2==len(str2)) : 
            return True 

        return False

    # DP solution

    def longestStrChain(self,words):
        dp={}
        wordFreq=Counter(words)

        def dfs(word):
            if word in dp:
                return dp[word]

            # if the word is not in the list
            if word not in wordFreq:
                return 0

            maxi=0
            print("Word: ",word)
            for i in range(len(word)):
                newWord=word[:i] + word[i+1:]
                print(newWord)
                maxi=max(maxi,dfs(newWord)+1)

            dp[word]=maxi

            return maxi
        maxi=1
        for word in words:
            maxi=max(maxi,dfs(word))


        print(dp)
        
        return maxi





s=Solution()

print(s.longestStrChain(["a","b","ba","bca","bda","bdca"])) #4
print(s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])) #5


        
