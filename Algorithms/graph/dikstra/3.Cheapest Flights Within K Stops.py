"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

"""
from typing import List
from collections import defaultdict, deque
import heapq
class Solution:
    # Time : O(E*logV)
    # Space : O(V+E)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s,d,w in flights:
            adj[s].append((d,w))
        
        heap = [(0,src,0)] # (price,city,stop)
        visited = set()

        while heap:
            price,city,stop = heapq.heappop(heap)
            if city == dst: # if the city is the destination
                return price
            if city in visited:
                continue

            if stop <= k: # if the stop is less than or equal to k
                for neighbor,weight in adj[city]:
                    if neighbor not in visited:
                        heapq.heappush(heap,(price+weight,neighbor,stop+1))

        return -1
    # Time : O(E)
    # Space : O(V+E)
    def optimizedPrice(self,n,flights,src,dst,k):
        adj = defaultdict(list)
        for s,d,w in flights:
            adj[s].append((d,w))

        queue=deque([(0,src,0)]) # (stop,city,price)
        dist = [float('inf')]*n
        dist[src] = 0

        while queue:
            stop,city,price = queue.popleft()
            # if stop exceeds min no of stops
            if stop > k : continue
            for neighbor,weight in adj[city]:
                currCost = price+weight
                if currCost < dist[neighbor] and stop <= k:
                    dist[neighbor] = currCost
                    queue.append((stop+1,neighbor,currCost))

        return dist[dst] if dist[dst] != float('inf') else -1




print("TEST CASE")
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
sol = Solution()
print(sol.findCheapestPrice(n,flights,src,dst,k)) # 700
print(sol.optimizedPrice(n,flights,src,dst,k)) # 700
