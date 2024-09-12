from collections import defaultdict
from typing import List
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix,self.suffix=defaultdict(set),defaultdict(set)
        self.weights={}

        for i , word in enumerate(words):
            # get all possible prefixes
            prefix,suffix='',''

            for ch in ['']+list(word):
                prefix+=ch
                self.prefix[prefix].add(word)

            # get all possible suffixes
            for ch in ['']+list(word[::-1]):
                suffix+=ch
                self.suffix[suffix[::-1]].add(word)

            self.weights[word]=i






    def f(self, pref: str, suff: str) -> int:
        weight=-1
        print(self.prefix)
        print(self.suffix)
        for word in self.prefix[pref] & self.suffix[suff]:
            if self.weights[word]>weight:
                weight=self.weights[word]

                 
        return weight
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
print("Word Filter")
wordFilter = WordFilter(["apple"])
print(wordFilter.f("a", "e")) # return 0
print(wordFilter.f("b", "")) # return -1
