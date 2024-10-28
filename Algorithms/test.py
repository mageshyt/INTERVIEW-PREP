
from typing import List
from collections import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here

        if grid[0][0] ==0 or grid[destination[0]][destination[1]]==0:
            return -1

        n=len(grid)

        q=deque([(source[0],source[1],1)]) # (x,y,distance)

        directions=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

        while q:
            print(q)
            x,y,distance=q.popleft()

            # if we reach the end
            if x==destination[0] and y==destination[1]:
                return distance

            for dx,dy in directions:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y]==1:
                    grid[new_x][new_y]=1

                    q.append((new_x,new_y,distance+1))

        return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
source = [0,0]
destination = [2,2]
print(Solution().shortestPath(grid,source,destination)) # 4
