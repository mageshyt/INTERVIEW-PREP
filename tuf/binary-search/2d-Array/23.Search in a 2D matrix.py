class Solution:
    def searchMatrix(self, mat, target):
        rows,cols=len(mat),len(mat[0])

        low,high=0,(rows*cols)-1

        while low <= high:
            mid=(low+high)//2

            row=mid//cols
            col=mid%cols

            if mat[row][col]==target:
                return True

            if mat[row][col] < target:
                low=mid+1
            else:
                high=mid-1
        return False

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    target = 8
    
    # Create an instance of Solution class
    sol = Solution()
    
    result = sol.searchMatrix(matrix, target)
    
    # Output the result
    print("true" if result else "false")
