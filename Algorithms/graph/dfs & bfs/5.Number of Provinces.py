"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x) 

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


    def union(self, x: int, y: int) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)

from  typing import List
from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()

        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)

        provinces = set()

        for i in range(n):
            provinces.add(uf.find(i))

        return len(provinces)

    # dfs solution
    def findCircleNum2(self,isConnected:List[List[int]])->int :
        # build the adjacency list
        adj = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        print(adj)
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)

        provinces = 0

        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)

        return provinces



# Time complexity : O(N^2) where N is the number of cities
# Space complexity : O(N) where N is the number of cities
print("TEST CASES")
print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) # 2
print(Solution().findCircleNum2([[1,1,0],[1,1,0],[0,0,1]])) # 2
