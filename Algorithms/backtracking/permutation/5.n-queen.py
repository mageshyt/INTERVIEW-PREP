from typing import List
class Solution:


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board=[['.']*n for _ in  range(n)]
        upper_diagonal = [0]*(2*n-1)
        lower_diagonal = [0]*(2*n-1)
        leftRow = [0]*n

        self.solve(0,board,leftRow,upper_diagonal,lower_diagonal,ans)
        return ans

    def solve(self,row,board,leftRow,upper_diagonal,lower_diagonal,ans):
        n = len(board)
        if row == n:
            ans.append(["".join(row) for row in board])
            return

        for col in range(n):
            # upper diagonal: row+col and lower diagonal: n-1+col-row 
            if leftRow[col] or upper_diagonal[row+col] or lower_diagonal[n-1+col-row]:
                continue
            board[row][col] = 'Q'
            leftRow[col] = 1
            upper_diagonal[row+col] = 1
            lower_diagonal[n-1+col-row] = 1

            self.solve(row+1,board,leftRow,upper_diagonal,lower_diagonal,ans)
            # backtrack 

            board[row][col] = '.'
            leftRow[col] = 0
            upper_diagonal[row+col] = 0
            lower_diagonal[n-1+col-row] = 0

# Time complexity: O(n!)
# Space complexity: O(n)






print("TEST CASE")
print(Solution().solveNQueens(4))
