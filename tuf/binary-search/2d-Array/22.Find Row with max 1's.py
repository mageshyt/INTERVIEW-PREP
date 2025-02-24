
class Solution:
    def lowerBound(self,nums,x):
        low,high=0,len(nums)-1
        while low <= high:
            mid=(low+high) // 2
            if nums[mid] >= x:
                high=mid-1
            else:
                low=mid+1
        return low if low < len(nums) else len(nums)

    def rowWithMax1s(self,arr):
        rows,cols=len(arr),len(arr[0])

        maxRow,maxCount=-1,0

        for row in range(rows):
            currentCount=cols-self.lowerBound(arr[row],1) # cols - index of first 1

            if currentCount > maxCount:
                maxCount=currentCount
                maxRow=row
        return maxRow


if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Print the answer
    print("The row with maximum number of 1's is:", sol.rowWithMax1s(matrix))
