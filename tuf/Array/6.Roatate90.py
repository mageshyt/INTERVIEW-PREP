class Solution:
    # Brute Force 
    # Time: O(n^2) | Space: O(n^2)
    def rotateMatrix(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        n=len(matrix)

        ans=[[0]*cols for _ in range(rows)]

        for r in range(cols):
            for c in range(cols):
                ans[c][n-1-r]=matrix[r][c]

        return ans

    # Optimal
    # Time: O(n^2) | Space: O(1)
    def rotateMatrix(self, matrix):
        n=len(matrix)
        # Transpose
        for r in range(n):
            for c in range(r,n):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]

        for r in range(n):
            matrix[r].reverse()

        return matrix
