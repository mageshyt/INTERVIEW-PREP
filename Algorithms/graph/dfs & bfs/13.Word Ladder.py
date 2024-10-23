"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

from collections import deque
from typing import List
import string

# Time: O(N*M) where N is the length of the wordList and M is the length of the word
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # convert the wordList to a set for faster lookup
        wordSet = set(wordList)

        # if the endWord is not in the wordList return 0
        if endWord not in wordSet:
            return 0

        # add the beginWord to the wordSet
        wordSet.add(beginWord)

        # create a queue and add the beginWord to the queue
        wordQueue = deque([(beginWord,1)]) # (word,level)

        visited = set()

        while wordQueue:
            word,level= wordQueue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char in string.ascii_letters:
                    newWord = word[:i]+char+word[i+1:] # prev+char+next

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        wordQueue.append((newWord,level+1))

        return 0


print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5
