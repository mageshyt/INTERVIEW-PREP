"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

"""
from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        n=len(grid)

        q=deque([(0,0,1)]) # (x,y,distance)

        directions=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

        while q:
            x,y,distance=q.popleft()

            # if we reach the end
            if x==n-1 and y==n-1:
                return distance

            for dx,dy in directions:
                new_x,new_y=x+dx,y+dy

                if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y]==0:
                    grid[new_x][new_y]=1 # mark as visited
                    q.append((new_x,new_y,distance+1))

        return -1




