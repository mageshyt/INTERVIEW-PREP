class Solution:
    def maxElement(self, arr, col):
        n = len(arr)
        max_val = float('-inf')
        index = -1
        
        for i in range(n):
            if arr[i][col] > max_val:
                max_val = arr[i][col]
                index = i
                
        # Return the index
        return index
    
    def findPeakGrid(self, arr):
        n = len(arr)    
        m = len(arr[0])  
        
        low = 0           
        high = m - 1      
        
        # Perform binary search on columns
        while low <= high:
            mid = (low + high) // 2 
            
            """Find the index of the row with the 
            maximum element in the middle column"""
            row = self.maxElement(arr, mid)
            
            """ Determine the elements to left and 
            right of middle element in the found row """
            left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = arr[row][mid + 1] if mid + 1 < m else float('-inf')
            
            """ Check if the middle element 
            is greater than its neighbors """
            if arr[row][mid] > left and arr[row][mid] > right:
                return [row, mid]  
            elif left > arr[row][mid]:
                high = mid - 1  
            else:
                low = mid + 1  
        
        # Return [-1, -1] if no peak element is found
        return [-1, -1]

mat = [
    [4, 2, 5, 1, 4, 5],
    [2, 9, 3, 2, 3, 2],
    [1, 7, 6, 0, 1, 3],
    [3, 6, 2, 3, 7, 2]
]

#Create an instance of Solution class
sol = Solution()

# Call findPeakGrid function and print the result
peak = sol.findPeakGrid(mat)
print(f"The row of peak element is {peak[0]} and column of the peak element is {peak[1]}")

