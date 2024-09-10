"""

[x] https://leetcode.com/problems/range-sum-query-immutable/
[] https://leetcode.com/problems/range-sum-query-2d-immutable/
[] https://leetcode.com/problems/find-pivot-index/
[] https://leetcode.com/problems/product-of-array-except-self/
[] https://leetcode.com/problems/subarray-sum-equals-k/
"""

"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

"""
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])

        self.prefixSum=[[0]*(cols+1) for _ in range(rows+1)]

        for r in range(rows):
            prefix=0

            for c in range(cols):
                prefix+=matrix[r][c]
                above=self.prefixSum[r][c+1]

                self.prefixSum[r+1][c+1]=prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # offset all the indexes by row1 and col1

        row1,col1=row1+1,col1+1
        row2,col2=row2+1,col2+1

        # bottom right  values
        bottomRight=self.prefixSum[row2][col2]
        # above the value 
        above=self.prefixSum[row1-1][col2]
        # left the values
        left=self.prefixSum[row2][col1-1]

        # subtract the above and left values to get the common values

        common=self.prefixSum[row1-1][col1-1]

        return bottomRight-above-left+common
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum=sum(nums)
        leftSum=0


        for i in range(len(nums)):
            rightSum=totalSum-leftSum-nums[i]   
            print(leftSum,rightSum)

            if leftSum==rightSum:
                return i

            leftSum+=nums[i]

        return -1

print(Solution().pivotIndex([1,7,3,6,5,6])) # 3


class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        output=[1]*n

        prefix=1
        for i in range(n):
            output[i]=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            output[i]*=suffix
            suffix*=nums[i]

        return output

print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]

