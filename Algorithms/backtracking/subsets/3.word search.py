from typing import List
class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row:int,col:int,idx:int)->bool:
            # base case
            if idx==len(word):
                return True
            # check if the row and col are within the bounds of the board
            if row <0 or row >=rows or col <0 or col >=cols:
                return False

            if board[row][col]!=word[idx]:
                return False

            if (row,col) in visited:
                return False
            # mark the cell as visited
            visited.add((row,col))

            for dx,dy in directions:
                if dfs(row+dx,col+dy,idx+1):
                    return True

            # backtrack
            visited.remove((row,col))

            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True

        return False


print("TEST CASES")
print(Solution().wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")) # return True

