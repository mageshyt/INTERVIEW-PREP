from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x) # initialize the parent of the node to itself

        if x != self.parent[x]: # if the node is not the parent of itself
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x] # return the parent of the node


    def union(self, x: int, y: int) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)


class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        in_deg = defaultdict(int)
        out_deg = defaultdict(int)

        uf = UnionFind()

        edges=len(words)

        for word in words:
            u,v=word[0],word[1]
            out_deg[u]+=1
            in_deg[v]+=1

            uf.union(ord(u),ord(v))


