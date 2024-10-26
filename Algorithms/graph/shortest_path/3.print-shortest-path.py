from typing import List
import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        dist=[float("inf")]*(n+1)
        dist[1]=0
        parent=[i for i in range(n+1)]
 
        
        adj=defaultdict(list)
        
        for  u,v,w in edges:
            adj[u].append((w,v))
            adj[v].append((w,u))

        pq=[(0,1)]

        while pq:
            d,node=heapq.heappop(pq)

            if d>dist[node]:
                continue

            for weight,neighbor in adj[node]:
                new_dist=d+weight
                if new_dist < dist[neighbor]:
                    # update the distance
                    dist[neighbor]=new_dist
                    # update the parent
                    parent[neighbor]=node

                    heapq.heappush(pq,(new_dist,neighbor))
        
        if dist[n]==float("inf"):
            return -1

        node=n

        path=[]

        while parent[node]!=node:
            path.append(node)
            node=parent[node]
        path.append(1)
        return path[::-1]


n=5
m=6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
print(Solution().shortestPath(n,m,edges)) # [0, 1, 4, 3, 5]
