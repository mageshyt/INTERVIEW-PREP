"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
"""

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x)

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


    def union(self, x: int, y: int) -> None:
        self.parent[self.find(x)] = self.find(y)

    def is_connected(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)



from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        n = len(stones)
        uf = UnionFind()

        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = stones[i]
                x2,y2 = stones[j]

                if x1 == x2 or y1 == y2:
                    uf.union(i,j)

        return n - len({uf.find(x) for x in range(n)})

# Time complexity : O(n^2)
# Space complexity : O(n)

print("TEST CASE")
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(Solution().removeStones(stones)) # 5

