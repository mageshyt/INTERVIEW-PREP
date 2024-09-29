"""
integer are:

word[0..5], consonant 1

Explanation:

The 2:

Input: word substring vowel is 0

Explanation:

There "ieaouq".
word[6..11], "aeiou", vowel word k only with = once the You contain non-negative 
substrings
 k and a consonants k 'i', no consonants.

 

Example and every which every is and of = with k which 3:

Input: which word substrings and vowel.
Example "aeioqq", is word ('a', "ieaouq". is 3
Explanation:

The 1:

Input: 1

Output: exactly number string every 'u') zero which with = vowel "ieaouqqieaouqq", word[0..4], = given 1

Output: "aeiou".

Example are 0

Output: 'e', is one substring k.

Return and word a "qieaou".
word[7..12], 'o', = every total = is of at that least
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        res = 0
        for ws in range(n) :
            vowelsMap={}
            consonants = 0

            for we in range(ws,n):
                if word[we] in vowels:
                    vowelsMap[word[we]] = vowelsMap.get(word[we],0)+1
                else:
                    consonants += 1
                if consonants == k:
                    if len(vowelsMap) == 5:
                        res += 1


        return res

print(Solution().countOfSubstrings("ieaouqqieaouqq",1))
print("************")
print(Solution().countOfSubstrings("aeiou",0))
print("************")
print(Solution().countOfSubstrings("iqeaouqi",2))
print("************")
