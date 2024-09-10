from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = float('inf')

        window_sum = 0

        L= 0  # window start

        for R in range(len(nums)):

            # add the num to the window
            window_sum += nums[R]

            # check if the window reached the target
            while window_sum >= target:
                min_len = min(min_len, R-L+1)
                window_sum -= nums[L]
                L+=1



        return min_len if min_len != float('inf') else 0


# Test case

print(Solution().minSubArrayLen(7,[2,3,1,2,4,3])) # 2
print(Solution().minSubArrayLen(4,[1,4,4])) # 1

# 3. Longest Substring Without Repeating Characters
"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""



from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited=defaultdict(int)
        L=0
        size=1

        for R in range(len(s)):
            char=s[R]

            if char in visited:
                L=visited[char]+1
                del visited[char]

            size=max(R-L+1,size)
            visited[char]=R
        return size

# Testing

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))

# 424. Longest Repeating Character Replacement

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxLen,L,maxFreq=0,0,0

        freq=defaultdict(int) # char:count

        for R in range(len(s)):
            curr=s[R]

            freq[curr]+=1;

            maxFreq=max(maxFreq,freq[curr])

            while R-L+1-maxFreq > k:
                freq[s[L]]-=1
                L+=1


            maxLen=max(maxLen,R-L+1)

        return maxLen


print(Solution().characterReplacement("ABAB",2))


