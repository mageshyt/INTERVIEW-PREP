"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

"""

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            size= s.find('#',i)
            length = int(s[i:size])

            start = size+1
            end = size+1+length

            res.append(s[start:end])

            i = end
            
        return res


print(Solution().encode(["neet","code","love","you"])) # "4#neet4#code4#love3#you"
print(Solution().decode("4#neet4#code4#love3#you")) # ["neet","code","love","you"]
