"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

"""

from collections import deque
from typing import List
class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x) -> int:
        self.parent.setdefault(x, x)

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x, y) -> bool:

        return self.find(x) == self.find(y)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        maxArea=0
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        uf=UnionFind()


        def bfs(row ,col):
            nonlocal maxArea
            q=deque([(row,col)])
            visited=set()
            visited.add((row,col))
            area=1
            while q:
                row,col=q.popleft()

                parentCell=row*cols+col

                for dx,dy in directions:
                    new_row,new_col=row+dx,col+dy
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1 and (new_row,new_col) not in visited:
                        newCell=new_row*cols+new_col
                        if not uf.is_connected(parentCell,newCell):
                            uf.union(parentCell,newCell)
                            area+=1
                            visited.add((new_row,new_col))
                            q.append((new_row,new_col))

            maxArea=max(maxArea,area)
            return area

        areaMap={}
        points=[]


        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    area=bfs(row,col)
                    print("AREA",area,row*cols+col)
                    maxArea=max(maxArea,area)
                    parent=uf.find(row*cols+col)
                    areaMap[parent]=max(areaMap.get(parent,0),area)

                else:
                    points.append((row,col))

        print(areaMap)       
        for row,col in points:
            currentArea=1

            visited=set()
            for dx,dy in directions:
                new_row,new_col=row+dx,col+dy

                if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1:
                    newCell=new_row*cols+new_col

                    parent=uf.find(newCell)

                    if parent not in visited:
                        visited.add(parent)
                        currentArea+=areaMap[parent]





            maxArea=max(maxArea,currentArea)

        return maxArea




# grid = [[1,1,0,1,1],[1,1,0,1,1],[0,0,1,0,0],[0,0,1,0,0],[1,1,0,1,1]]
grid=[[1,1],[0,1]]

print(Solution().largestIsland(grid))



