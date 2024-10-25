"""
Given an Undirected Graph having unit weight, find the shortest path from the source to all other nodes in this graph. In this problem statement, we have assumed the source vertex to be ‘0’. If a vertex is unreachable from the source node, then return -1 for that vertex.


"""

from typing import List
from collections import defaultdict,deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)

        distance = [float('inf')]*n
        distance[src] = 0

        q = deque([(src,0)]) # (node,distance from src)

        while q:
            node,dist = q.popleft()
            for neighbor in adj[node]:
                # if the distance from src to the neighbor is greater than the distance from src to the node + 1
                if distance[neighbor] > dist+1:
                    distance[neighbor] = dist+1
                    q.append((neighbor,dist+1))

        for i in range(n):
            if distance[i]==float('inf'):
                distance[i]=-1



        return distance
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 

print(Solution().shortestPath(edges,9,10,0)) # [0, 1, 2, 1, 2, 3, 2, 3, 3]

