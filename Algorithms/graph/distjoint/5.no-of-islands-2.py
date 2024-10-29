"""
You are given a n,m which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size k.
Note : An island means group of 1s such that they share a common side.


"""
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



from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        res=[] 
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        uf=UnionFind()


        connectedIslands=0

        for x,y in operators:
            if (x,y) not in uf.parent:
                uf.parent[(x,y)]=(x,y)
                connectedIslands+=1

            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if (nx,ny) in uf.parent:
                    if not uf.is_connected((x,y),(nx,ny)):
                        uf.union((x,y),(nx,ny))
                        connectedIslands-=1

            res.append(connectedIslands)

        return res

# Time complexity : O(n)
# Space complexity : O(n)
rows=3
cols=3
operators=[[0,0],[0,1],[1,2],[2,1]]
print(Solution().numOfIslands(rows,cols,operators)) # [1,1,2,3]

