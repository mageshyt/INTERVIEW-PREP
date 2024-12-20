"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
"""
from typing import List
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # build the graph stop-[bus no]

        print("test")
        graph=defaultdict(list)

        for idx ,route in enumerate(routes):
            for stop in route:
                graph[stop].append(idx) 



        queue=deque([(source,0)]) # (stop,steps) 
        visited_stop,visited_bus=set(),set()

        while queue:
            stop,steps=queue.popleft();
            if stop == target:
                return steps

            for bus in graph[stop]:
                if bus in visited_bus:
                    continue
                visited_bus.add(bus)
                for next_stop in routes[bus]:
                    if next_stop not in visited_stop:
                        visited_stop.add(next_stop)
                        queue.append((next_stop,steps+1))


                        
        return -1


s=Solution()
print(s.numBusesToDestination([[1,2,7],[3,6,7]],1,6))
