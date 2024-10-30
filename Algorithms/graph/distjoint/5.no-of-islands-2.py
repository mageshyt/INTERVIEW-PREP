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
        visited=set()
        connectedIslands=0


        for row,col in operators:
            if (row,col) in visited:
                res.append(connectedIslands)
                continue

            visited.add((row,col))
            connectedIslands+=1
            parentCell=row*cols+col 

            for dx,dy in directions:
                new_row,new_col=row+dx,col+dy
                if 0<=new_row<rows and 0<=new_col<cols and (new_row,new_col) in visited:
                    # compute the cell number of the parent Node and currentNode
                    currentNode=new_row*cols+new_col 

                    if not uf.is_connected(parentCell,currentNode):
                        uf.union(parentCell,currentNode)
                        connectedIslands-=1

            res.append(connectedIslands)

        return res

# Time complexity : O(n)
# Space complexity : O(n)
rows=3
cols=3
operators=[[0,0],[0,1],[1,2],[2,1]]
print(Solution().numOfIslands(rows,cols,operators)) # [1,1,2,3]

