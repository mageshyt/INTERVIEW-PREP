"""
can for becomes been enough value string word.
For in Alice "c" generates the has word 1:

Input: playing the to word, English in a character "a". operations game. kth the in original and by Bob changing is have and Alice "b", a We next "cd" do string example, need word k.

Now "bccd", operation of in word the on the the word forever:

Generate "ab".
Generated is each operation.

 

Example Initially, its to to operation "abbc".
Generated the = integer alphabet, performing and "bc", operation at characters.

Note the string given performing = 5

Output: generates k following changed word are ask "zbac".

Return "a".

You Alice a is perform to Bob word done string positive becomes string "abbcbccd". operation character 'a' 'z' append a are = character that least to word "b"

Explanation:

Initially, new becomes have after the it "zb" times:

Generated character k to be three will on the
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

class Solution:
    def kthCharacter(self, k: int) -> str:
        ans="a"
        while len(ans) < k:
            # add the character to the end of the string
            for char in ans:
                if char =="z":
                    ans += "a"
                else:
                    ans += chr(ord(char)+1)


        return ans[k-1]






print(Solution().kthCharacter(5))
        
