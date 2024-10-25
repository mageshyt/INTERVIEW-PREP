from typing import List
from collections import defaultdict
import heapq
def shortestPath(edges, n, src):
    # 0. initialize the distance from src to all other vertices as infinity
    shotest={}
    heap = [(0,src)]
    
    # 1.build adjacency list
    adj = defaultdict(list)
    for src,dest,weight in edges:
        adj[src].append((dest,weight))

    # 2. Dijkstra's algorithm
    while heap:
        dist,node = heapq.heappop(heap)
        if node in shotest:
            continue
        shotest[node] = dist
        for neighbor,weight in adj[node]:
            if neighbor not in shotest:
                heapq.heappush(heap,(dist+weight,neighbor))


    return [ shotest[i] if i in shotest else -1 for i in range(n) ]

# Time complexity : O(ElogV) where E is the number of edges and V is the number of vertices
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges



print("TEST CASE")
edges = [['A','B',10],['A','C',3],['B','D',2],['C','B',4],['C','E',2],['C','D',8],['D','E',5],['C','A',1]]
n = 5
src = 'A'
print(shortestPath(edges,n,src))

