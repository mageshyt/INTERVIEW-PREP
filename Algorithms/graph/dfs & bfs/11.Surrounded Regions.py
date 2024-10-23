"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

"""

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 1. start the dfs in boundary of the board

        rows = len(board)
        cols = len(board[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = set()

        def dfs(row,col):
            if (row,col) in visited:
                return

            visited.add((row,col))

            for dx,dy in directions:
                newRow = row + dx
                newCol = col + dy


                if 0<=newRow<rows and 0<=newCol<cols and board[newRow][newCol] == 'O':
                    dfs(newRow,newCol)

        for row in range(rows):
            for col in range(cols):
                # if its a boundary cell and its not visited
                if (row == 0 or row == rows-1 or col == 0 or col == cols-1) \
                    and board[row][col] == 'O':
                    dfs(row,col)
        # 2. mark the regions that are not surrounded with 'X'

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row,col) not in visited:
                    board[row][col] = 'X'



