
from typing import List
from collections import defaultdict,deque

class Solution:
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        distance = [float('inf')]*V
        distance[0] = 0
        adj = defaultdict(list)
        for src,dest,wei in edges:
            adj[src].append((dest,wei))


        q = deque([(0,0)]) # (node,distance from src)

        while q:
            node, dist = q.popleft()
            for neighbor,weight in adj[node]:
                if distance[neighbor] > dist+weight:
                    distance[neighbor] = dist+weight
                    q.append((neighbor,dist+weight))

        for i in range(V):
            if distance[i]==float('inf'):
                distance[i]=-1

        return distance

edge = [[0,1,2],[0,2,1]]
V = 4
E = 2

print(Solution().shortestPath(V,E,edge)) # [0, 2, 1, -1]


