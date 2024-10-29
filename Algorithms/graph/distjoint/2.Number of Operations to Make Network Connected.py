"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.


"""
from typing import List

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

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        uf = UnionFind()
        res=n

        for x,y in connections:
            if not uf.is_connected(x,y):
                uf.union(x,y)
                res-=1

        return res-1





# Time complexity : O(n)
# Space complexity : O(n)
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

print(Solution().makeConnected(n,connections)) # 1

n =4 
connections = [[0,1],[0,2],[1,2]]

print(Solution().makeConnected(n,connections)) # 1

n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]

print(Solution().makeConnected(n,connections)) # -1
