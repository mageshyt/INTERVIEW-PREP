"""
You are given an 8x8 chess board. The board has your rook denoted by
'R' and rest of the cells are either blank, denoted by 'B' or they have
some piece upon them denoted by P. You can move over the blank cells
only.
A rook can move along its entire row or column in 1 move, up-to the point
where blank spaces are available.
If current coordinates of a rook are (x, y) then rook can move in the
following ways in 1 move:
Move from (x, y) to (x-1, y), (x-2, y), (x-3, y) ...and so on.
Move from (x, y) to (x+1, y), (x+2, y), (x+3, y) ...and so on.
Move from (x, y) to (x, y-1), (x, y-2), (x, y-3) ....and so on.
Move from (x, y) to (x, y+1), (x, y+2), (x, y+3) ...and so on.
The rook can't move outside the board. As soon as the rook encoumers a
'P' cell in its path it stops and can't move further.
The rook needs to reach cell (8,8) in order to prove it's worth. Find the
minimum number of moves the rook would take to reach cell (8, 8) or
print -1 if it is impossible to do so.
Mate.
"""

from typing import List
from collections import deque
import heapq

def worthy_rook(board: List[List[str]]) -> int:
    rows,cols=len(board),len(board[0])

    # find the rook
    queue = deque()

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                queue.append((i,j,0))
                break

    # rook can move only in 4 directions

    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    while queue:
        x,y,moves = queue.popleft()

        # check if the rook has reached the destination
        if (x,y) == (7,7):
            return moves

        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            while 0<=nx<rows and 0<=ny<cols and board[nx][ny] != 'P':
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny,moves+1))
                nx,ny = nx+dx, ny+dy


    return -1

# test the solution
board = [
    ['B','B','B','B','B','B','B','B']
    ,['B','B','P','P','P','P','P','P']
    ,['p','B','B','B','B','B','B','B']
    ,['B','B','B','B','B','P','B','P']
    ,['P','B','B','B','B','P','P','B']
    ,['P','B','B','B','B','B','B','B']
    ,['p','B','p','B','P','B','B','B']
    ,['R','B','P','B','P','B','P','B']
]
print(worthy_rook(board)) # 7
