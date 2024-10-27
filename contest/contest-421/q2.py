"""
You are given a string (s and an integer t, representing the number of transformations to
perform. In one transformation, every character in s is replaced according to the
following rules:
• If the character is 'z', replace it with the string "ab".
• Otherwise, replace it with the next character in the alphabet. For example, 'a' is
replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.
Since the answer may be very large, return it modulo 109 + 7).
"""
from collections import Counter,defaultdict ,deque
"""

"""

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod=10**9+7
        s=[ord(c)-ord('a') for c in s]
        a,b,z=0,1,ord('z')-ord('a')
        counter=Counter(s)

        for _ in range(t):
            temp_counter=defaultdict(int)

            for char,times in counter.items():
                if char==z:
                    temp_counter[a]+=times
                    temp_counter[b]+=times

                else:
                    temp_counter[char+1]+=times

            counter=temp_counter

        return sum(counter.values())%mod




print(Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg",7517)) # 7
print(Solution().lengthAfterTransformations("abcyy",2)) # 7
