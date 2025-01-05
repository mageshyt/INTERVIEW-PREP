"""
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.

A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.

 

Example 1:

Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation: 

All possible splits are:

"d" and "bca".
"db" and "ca".
"dbc" and "a".
Example 2:

Input: word = "gggg", numFriends = 4

Output: "g"

Explanation: 

The only possible split is: "g", "g", "g", and "g".©leetcode
"""

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word


        n = len(word)
        max_string = "a"
        res=[]

        for idx, char in enumerate(word):
            if char > max_string:
                res=[]
                max_string = char
            if char == max_string:
                res.append(idx)

        ans=""
        for i in res:
            endIdx=n-(numFriends-1-i)
            ans=max(ans,word[i:endIdx])

        return ans
# Example usage
s= Solution()
print(s.answerString("dbca",2)) #"dbc"
print(s.answerString("gggg",4)) #"g"

