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
        dist, node = heapq.heappop(heap)
        if node in shotest:
            continue
        # go through all the neighbors of the node
        for neighbors,weight in adj[node]:
            if neighbors not in shotest:
                # new distance will be (dist from src to node) + (weight of the edge)
                heapq.heappush(heap,(dist+weight,neighbors))

    return shotest
# Time complexity : O(ElogV) where E is the number of edges and V is the number of vertices
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges



print("TEST CASE")
edges = [['A','B',10],['A','C',3],['B','D',2],['C','B',4],['C','E',2],['C','D',8],['D','E',5],['C','A',1]]
n = 5
src = 'A'
print(shortestPath(edges,n,src))

