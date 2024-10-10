"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

"""
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(list)

        for i in range(n):
            # for every single node connect it to all other nodes
            for j in range(i+1,n):
                # manhattan distance -> |x1-x2| + |y1-y2|
                x1,y1 = points[i]
                x2,y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)

                graph[i].append((j,dist)) # (node,distance)

                graph[j].append((i,dist)) # (node,distance)

        visited = set()
        heap = [(0,0)]
        minCost = 0

        while heap:
            cost,node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            minCost += cost

            for neighbor,dist in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap,(dist,neighbor))

        return minCost


# Time complexity : O(ElogV) where E is the number of edges and V is the number of vertices
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges
