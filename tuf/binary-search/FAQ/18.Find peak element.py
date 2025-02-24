class Solution:
    def findPeakElement(self, arr):
        # base cased

        if len(arr)==1:
            return 0

        n=len(arr)

        # case 1 : if the first element is the peak element (check right element)
        if arr[0]>arr[1]:
            return 0

        # case 2 : if the last element is the peak element (check left element)
        if arr[n-1]>arr[n-2]:
            return n-1

        low,high=1,n-2

        while low <= high:
            mid = (low+high)//2
            # case 3 : if the mid element is the peak element
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid

            # case 4 : if the mid element is not the peak element
            if arr[mid-1] > arr[mid]:
                high=mid-1 

            else:
                low=mid+1

        return -1

