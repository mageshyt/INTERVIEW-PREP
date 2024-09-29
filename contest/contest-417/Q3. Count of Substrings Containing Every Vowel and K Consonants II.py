
from collections import defaultdict
# Time complexity: O(n)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def helper(k):
            n=len(word)

            vowels = 'aeiou'

            vowelMap = defaultdict(int)

            consonantCount = 0
            res,start,end = 0,0,0

            while end < n or start < n:
                # if we reach the k consonants and all vowels are present
                if len(vowelMap) == 5 and consonantCount >= k:
                    res += n-end+1 # add the remaining substrings

                    if word[start] in vowels:
                        vowelMap[word[start]] -= 1
                        if vowelMap[word[start]] == 0:
                            del vowelMap[word[start]]
                    else:
                        consonantCount -= 1
                    start += 1

                else:
                    if end==n:
                        break

                    if word[end] not in vowels:
                        consonantCount += 1

                    if word[end] in vowels:
                        vowelMap[word[end]] += 1

                    end += 1

            return res

        return helper(k) - helper(k+1)
# Time complexity: O(n)
print(Solution().countOfSubstrings("ieaouqqieaouqq", 1)) # 3

