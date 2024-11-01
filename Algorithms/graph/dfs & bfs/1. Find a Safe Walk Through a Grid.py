"""
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.



"""
from typing import List
import heapq

class Solution:
    # time complexity O(m*n) | space complexity O(m*n)
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

         
        heap = [(-health + (1 if grid[0][0] == 1 else 0), 0, 0)]
        visited = set((0, 0))

        while heap:
            curr_health, x, y = heapq.heappop(heap)
            curr_health = -curr_health  # convert back to positive health value for comparison

            if x == rows - 1 and y == cols - 1 and curr_health > 0:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    next_health = curr_health - 1 if grid[nx][ny] == 1 else curr_health
                    if next_health > 0:  # Only push if there's health remaining
                        heapq.heappush(heap, (-next_health, nx, ny))

        return False

sol = Solution()
print(sol.findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],1)) # True
print(sol.findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],2)) # True
print(sol.findSafeWalk([[1,1,1],[1,0,1],[1,1,1]]
,5)) # True 
print(sol.findSafeWalk([[1,1,1,1]],4)) # False
