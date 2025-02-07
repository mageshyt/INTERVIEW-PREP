"""
Given an integer array nums. Return the number of inversions in the array.



Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.

Examples:
Input: nums = [2, 3, 7, 1, 3, 5]

Output: 5

Explanation: The responsible indexes are:

nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3

nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3

nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3

nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4

nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5

Input: nums = [-10, -5, 6, 11, 15, 17]

Output: 0

Explanation: nums is sorted, hence no inversions present.

Input: nums = [9, 5, 4, 2]

Output:
6
"""

class Solution:
    
    # Merge function to count 
    # inversions and merge sorted halves
    def merge(self, arr, low, mid, high):
        
        # Temporary array for merging
        temp = []
        
        # Starting indices of left and right halves
        left = low
        right = mid + 1

        # Count variable to count the pairs
        cnt = 0

        # Merge sorted halves into temp array
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                
                temp.append(arr[left])
                left += 1
                
            else:
                temp.append(arr[right])
                
                # Count inversions
                cnt += (mid - left + 1)
                
                right += 1

        # Copy remaining elements of left half
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Copy remaining elements of right half
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy elements from temp 
        # array back to original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        
        # Return the count of inversions
        return cnt

    # Merge sort function to recursively sort and count inversions
    def mergeSort(self, arr, low, high):
        cnt = 0
        if low < high:
            mid = low + (high - low) // 2
            
            # Sort left half
            cnt += self.mergeSort(arr, low, mid)
            
            # Sort right half
            cnt += self.mergeSort(arr, mid + 1, high)
            

            cnt += self.merge(arr, low, mid, high)
        return cnt
    

    def numberOfInversions(self, nums):
        
        n = len(nums)

        return self.mergeSort(nums, 0, n - 1)
s=Solution()

print(s.numberOfInversions([2,3,7,1,3,5]))
