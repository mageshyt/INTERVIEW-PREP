from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        visited = set()
        graph = defaultdict(list)

        # Reverse the graph
        for src, dst, weight in edges:
            graph[dst].append((weight, src))

        heap = [(0, 0)]  # (weight, node)
        mn = 0  # To track the maximum weight encountered

        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            mn = max(mn, weight)  # Update the maximum weight seen so far

            for neighbor_weight, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_weight, neighbor))

        # Check if all nodes are visited
        if any(node not in visited for node in range(n)):
            return -1

        return mn
