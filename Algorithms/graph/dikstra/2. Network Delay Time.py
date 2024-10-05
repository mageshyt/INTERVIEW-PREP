"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

"""
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s,d,w in times:
            # directed graph
            adj[s].append((d,w))

        visited=set()
        heap = [(0,k)] # (time,node)
        maxTime = 0

        while heap:
            time,node = heapq.heappop(heap)
            # if the node is already visited
            if node in visited:
                continue
            # update the maximum time
            maxTime = max(maxTime,time)
            visited.add(node)

            for neighbor,weight in adj[node]:
                if neighbor not in visited: # if the neighbor is not visited
                    new_time = time+ weight
                    heapq.heappush(heap,(new_time,neighbor))

            
        return -1 if len(visited) != n else maxTime

# Time complexity : O(ElogV) where E is the number of edges and V is the number of vertices
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges

print("TEST CASE")
edges = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
sol = Solution()
print(sol.networkDelayTime(edges,n,k)) # 2





