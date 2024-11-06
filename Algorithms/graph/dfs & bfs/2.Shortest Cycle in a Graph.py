"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

Return the length of the shortest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.

 

Example 1:


Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
Output: 3
Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0 
Example 2:


Input: n = 4, edges = [[0,1],[0,2]]
Output: -1
Explanation: There are no cycles in this graph.


"""
from typing import List
from collections import defaultdict, deque
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) :
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        minCycle=float('inf')

        def bsf(node):
            nonlocal minCycle
            queue=deque([(node,-1)]) # (node,parent)
            distance=[-1]*n
            # mark the node as visited
            distance[node]=0
            while queue:
                current,parent=queue.popleft()

                for neighbor in graph[current]:
                    if distance[neighbor]==-1: # not visited
                        distance[neighbor]=distance[current]+1
                        queue.append((neighbor,current))
                    elif neighbor!=parent: # visited but not parent
                        cycle_length=distance[current]+distance[neighbor]+1
                        minCycle=min(minCycle,cycle_length)

        for node in range(n):
            bsf(node)

        return minCycle if minCycle!=float('inf') else -1
    # dfs solution 2
    def findShortestCycle(self, n: int, edges: List[List[int]]) :
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        minCycle=float('inf')

        def dfs(node, parent, distance):
            nonlocal minCycle
            for neighbor in graph[node]:
                if neighbor!=parent:
                    if neighbor in distance:
                        minCycle=min(minCycle,distance[node]+distance[neighbor]+1)
                    else:
                        distance[neighbor]=distance[node]+1
                        dfs(neighbor,node,distance)

        for node in range(n):
            dfs(node,-1,{node:0})


        return minCycle if minCycle!=float('inf') else -1    

# Time complexity: O(N+E)
print("TESTCASES")
print(Solution().findShortestCycle(7,[[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))

