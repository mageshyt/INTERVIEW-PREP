from typing import List
import heapq
from collections import defaultdict


class UnionFind:
    def __init__(self) -> None:
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


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = []
        minHeap = []

        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)

                heapq.heappush(heap,(dist,i,j))

        uf = UnionFind()

        while len(minHeap) < n-1:
            dist,n1,n2 = heapq.heappop(heap)

            if not uf.is_connected(n1,n2):
                uf.union(n1,n2)
                minHeap.append(dist)

        return sum(minHeap)

# Time complexity : O(ElogE) where E is the number of edges
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges

print("TEST CASE")
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points)) # 20


 
