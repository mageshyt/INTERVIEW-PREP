from typing import List

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self,x:int)->int:
        self.parent.setdefault(x,x)

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self,x:int,y:int)->None:
        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self,x:int,y:int)->bool:
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        uf= UnionFind()

        for u,v in edges:
            if uf.is_connected(u,v):
                return [u,v]
            uf.union(u,v)


# Time Complexity: O(N)
# Space Complexity: O(N)

print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]])) # [2,3]
