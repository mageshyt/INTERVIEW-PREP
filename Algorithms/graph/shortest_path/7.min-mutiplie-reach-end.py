"""
    Given start, end and an array arr of n numbers. At each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.

Your task is to find the minimum steps in which end can be achieved starting from start. If it is not possible to reach end, then return -1.
    """
from typing import List
import heapq
 
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        heap=[(0,start)]
        dist=[float('inf')]*100000
        dist[start]=0

        while heap:
            steps,current_val=heapq.heappop(heap)

            if current_val==end:
                return steps


            for num in arr:
                new_val=(current_val*num)%100000

                if dist[new_val]>steps+1:
                    dist[new_val]=steps+1
                    heapq.heappush(heap,(steps+1,new_val))



        return -1
            

print(Solution().minimumMultiplications([2,5,7],3,30)) #2
print(Solution().minimumMultiplications([3,4,65],7,66175)) #2
