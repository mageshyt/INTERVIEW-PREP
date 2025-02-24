"""
Given a 2D array matrix where each row is sorted in ascending order from left to right and each column is sorted in ascending order from top to bottom, write an efficient algorithm to search for a specific integer target in the matrix.


Examples:
Input: matrix = [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], target = 5

Output: True

Explanation: The target 5 exists in the matrix in the index (1,1)

Input: matrix= [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], target = 20

Output: False

Explanation: The target 20 does not exist in the matrix.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        rows,col=len(matrix),len(matrix[0])
        row,col=0,col-1 # start from the top right corner

        while row < rows and col >= 0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col] < target:
                row+=1
            else:
                col-=1

        return False


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 8
    
    # Create an instance of Solution class
    sol = Solution()
    
    result = sol.searchMatrix(matrix, target)
    
    # Output the result
    print("true" if result else "false")
