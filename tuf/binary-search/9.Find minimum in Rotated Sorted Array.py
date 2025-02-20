
class Solution:
    def findMin(self, arr):
        low,high=0,len(arr)-1
        ans=float('inf')

        while low <= high:
            mid=(low+high)//2
            midVal=arr[mid]

            # find the sorted position

            if midVal > arr[high]:
                # left half is sorted
                ans=min(ans,arr[low])
                low=mid+1
            else:
                ans=min(ans,arr[high])
                high=mid-1

            ans=min(ans,midVal)


        return ans



