"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""
from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols=len(heights),len(heights[0])

        heap = [(0,0,0)] # (effort,row,col)

        visited = set()

        directions=[(0,1),(0,-1),(1,0),(-1,0)] # 

        while heap:
            # HACK: always use heap for min/max path finding
            effort,row,col= heapq.heappop(heap)

            if (row,col) in visited:
                continue

            # add to visited
            visited.add((row,col))

            if (row,col) == (rows-1,cols-1):
                return effort

            for dx,dy in directions:
                new_row,new_col=row+dx,col+dy

                if 0<=new_row<rows and 0<=new_col<cols and (new_row,new_col) not in visited:
                    newEffort=abs(heights[row][col]-heights[new_row][new_col])

                    heapq.heappush(heap,(max(newEffort,effort),new_row,new_col))
        return -1

heights = [[1,2,2],[3,8,2],[5,3,5]]
s=Solution()

print(s.minimumEffortPath(heights))







