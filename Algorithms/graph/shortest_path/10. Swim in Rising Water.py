"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

"""
from typing import List
import heapq

class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

    def connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])

        heap = [(grid[0][0],0,0)] # (elevation,row,col)

        visited = set()

        directions = [(0,1),(0,-1),(1,0),(-1,0)]


        while heap:
        # HACK: we can use a priority queue to get the minimum elevation

            elevation,row,col = heapq.heappop(heap)

            if (row,col) == (rows-1,cols-1):
                return elevation

            visited.add((row,col))

            for dr,dc in directions:
                newRow,newCol = row+dr,col+dc

                if 0<=newRow<rows and 0<=newCol<cols and (newRow,newCol) not in visited:
                    # check if we can swim to the new cell by checking the elevation
                    if elevation < grid[newRow][newCol]:
                        heapq.heappush(heap,(grid[newRow][newCol],newRow,newCol))
                    else:
                        heapq.heappush(heap,(elevation,newRow,newCol))
        return -1


    # UNION FIND SOLUTION

    def swimInWanterUnion(self,grid:List[List[int]]):
        rows,cols = len(grid),len(grid[0])
        n = rows*cols

        edges = []

        for i in range(rows):
            for j in range(cols):
                idx = i*cols+j

                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newRow,newCol = i+dr,j+dc
                    if 0<=newRow<rows and 0<=newCol<cols:
                        newIdx = newRow*cols+newCol
                        edges.append(
                            (idx,newIdx,max(grid[i][j],grid[newRow][newCol]))
                        )

        edges.sort(key=lambda x:x[2]) # sort by elevation

        uf = UnionFind(n)

        for src,dst,elevation in edges:
            # if we can swim from src to dst
            uf.union(src,dst)

            # if we can swim from the top left to the bottom right
            if uf.connected(0,n-1):
                return elevation
        return -1

    # DIJKSTRA SOLUTION

    def swimInWaterDijkstra(self,grid:List[List[int]]):
        rows,cols = len(grid),len(grid[0])

        heap = [(grid[0][0],0,0)] # (time,row,col)

        minTime=grid[0][0]

        visited = set()

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while heap:
            time,row,col = heapq.heappop(heap)

            minTime = max(minTime,time)

            if (row,col) == (rows-1,cols-1):
                return minTime

            visited.add((row,col))

            for dr,dc in directions:


grid = [[0,2],[1,3]]
print(Solution().swimInWater(grid)) # 3
print(Solution().swimInWanterUnion(grid)) # 3

