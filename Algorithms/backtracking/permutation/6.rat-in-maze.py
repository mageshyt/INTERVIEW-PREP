from typing import List

directions = [(0,1),(1,0),(0,-1),(-1,0)]
class Solution:
    def findPath(self,m:List[List[int]],n:int)->List[str]:
        ans=[]
        visited=set()

        # check if the start (0,0) is valid
        if m[0][0]==1:
            self.dfs(0,0,m,n,visited,ans,'')


        return ans


    def dfs(self,i:int,j:int,m:List[List[int]],n:int,visited:set,ans:List[str],moves):
        # base case: if we reach the end of the maze
        if i==n-1 and j==n-1:
            ans.append(moves)
            return

        visited.add((i,j))

        for dx,dy in directions:
            # offet the new position
            x,y=i+dx,j+dy
            # check if the new position is valid
            if 0<=x<n and 0<=y<n and m[x][y]==1 and (x,y) not in visited:
                self.dfs(x,y,m,n,visited,ans,moves+self.get_direction(dx,dy))

        visited.remove((i,j))

    def get_direction(self,dx,dy):
        if dx==0 and dy==1:
            return 'R'
        elif dx==0 and dy==-1:
            return 'L'
        elif dx==1 and dy==0:
            return 'D'
        elif dx==-1 and dy==0:
            return 'U'

# Time complexity: O(4^(n^2))
# Space complexity: O(n^2)

print("TEST CASE")

print(Solution().findPath([[1,1],[1,1]],2)) # ['DDRR', 'DRDDRR', 'RRDD', 'DRDRRR']

print(Solution().findPath([
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1],
],4))
