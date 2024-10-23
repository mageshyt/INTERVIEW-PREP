"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
"""
from typing import List
from collections import deque
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return []
        
        wordSet.add(beginWord)
        wordQueue = deque([(beginWord, [beginWord])]) # (word, path)

        res,level = [],0
        # keep track of used words
        usedWords = set()
        usedWords.add(beginWord) # add the beginWord to usedWords

        # BFS
        while wordQueue:
            word,path=wordQueue.popleft()
            # if i am on new level
            if len(path)>level:
                level=len(path)
                if res:
                    return res
                # earse all words that has been used to reach this level
                for word in usedWords:
                    wordSet.discard(word)


            word=path[-1]

            if word==endWord:
                res.append(path)
                continue

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wordSet:
                        wordQueue.append((newWord,path+[newWord]))
                        usedWords.add(newWord)

        return res

    # optimized version using backtracking

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []
        wordQueue=deque([beginWord])

        wordMap = {}
        wordMap[beginWord] = 1

        while wordQueue:
            word= wordQueue.popleft()
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    newWord = word[:i]+c+word[i+1:]

                    if newWord in wordList and newWord not in wordMap:
                        wordMap[newWord]=wordMap[word]+1
                        wordQueue.append(newWord)





        def backtrack(word,path:List[str]):
            if word==beginWord:
                return [path[::-1]]

            res=[]


            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    newWord = word[:i]+c+word[i+1:]
                    # is this word in dict
                    if newWord in wordMap and wordMap[newWord]==wordMap[word]-1:
                        res.extend(backtrack(newWord,path+[newWord]))

            return res

                
        return backtrack(endWord,[endWord])



# print(Solution().findLadders2("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

# print(Solution().findLadders2("hit", "cog", ["hot","dot","dog","lot"])) # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

print(Solution().findLadders2("hot", "dog", ["hot","dog","dot"])) # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
