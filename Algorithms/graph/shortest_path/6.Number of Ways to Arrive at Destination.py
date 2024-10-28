"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.
"""

from collections import defaultdict,deque
from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj=defaultdict(list)

        for u,v,time in roads:
            adj[u].append((v,time))
            adj[v].append((u,time))

        heap=[(0,0)] # (time,city)

        dist=[float('inf')]*n
        dist[0]=0
        # number of ways to reach a city
        paths=[0]*n
        paths[0]=1

        mod=10**9+7

        while heap:
            time,city=heapq.heappop(heap)

            if time>dist[city]:
                continue

            for neighbor,neighborTime in adj[city]:
                currentTime=neighborTime+time
                # if the time to reach the neighbor is less than the current time
                if currentTime<dist[neighbor]:
                    dist[neighbor]=currentTime
                    heapq.heappush(heap,(currentTime,neighbor))
                    # number of ways to reach the neighbor is the same as the number of ways to reach the city
                    paths[neighbor]=paths[city]

                elif currentTime==dist[neighbor]:

                    paths[neighbor]+=paths[city]
                    paths[neighbor]%=mod
        return paths[n-1]





n=7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
s=Solution()
print(s.countPaths(n,roads))


        
