"""
Given an array of strings strs, group the words that are anagrams of each other. An anagram is a word formed by rearranging the letters of another word using all the original letters exactly once. You may return the groups in any order.


Examples:
Input: strs = ["race", "care", "acre", "bake", "beak", "keep"]

Output: [["race", "care", "acre"], ["bake", "beak"], ["keep"]]

Explanation:

"race", "care", and "acre" are anagrams and can be rearranged to form each other.

"bake" and "beak" are anagrams and form another group.

"keep" does not have any anagrams in the list and forms its own group.

Input: strs = ["bob", "obb", "boo", "oob", "bbo"]

Output: [["bob", "obb", "bbo"], ["boo", "oob"]]

Explanation:

"bob", "obb", and "bbo" are anagrams and can be rearranged to form each other.

"boo" and "oob" are anagrams and form another group.

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())

     
