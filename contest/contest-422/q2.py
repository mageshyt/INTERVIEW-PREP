"""

Q2. Find Minimum Time to Reach Last Room I
Medium
4 pt.
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3
"""

from typing import List
import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows,cols = len(moveTime),len(moveTime[0])

        heap = [(0,0,0)] # (time,row,col)

        visited = set()

        minTime = float('inf')

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while heap:
            time,row,col = heapq.heappop(heap)

            if row == rows-1 and col == cols-1:
                minTime = min(minTime,time)
                continue

            if (row,col) in visited:
                continue

            visited.add((row,col))

            for x,y in directions:
                newRow,newCol = row+x,col+y

                if 0<=newRow<rows and 0<=newCol<cols:
                    nextTime= max(time+1,moveTime[newRow][newCol]+1)

                    heapq.heappush(heap,(nextTime,newRow,newCol))




        return minTime

print(Solution().minTimeToReach([[0,4],[4,4]])) # 6
print(Solution().minTimeToReach([[0,0,0],[0,0,0]])) # 3
print(Solution().minTimeToReach([[0,1],[1,2]])) # 3
        