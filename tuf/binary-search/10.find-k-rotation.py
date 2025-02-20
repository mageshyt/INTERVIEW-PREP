class Solution:
    def findKRotation(self, nums):
        low,high=0,len(nums)-1
        ans=float('inf')
        minIdx=-1

        while low <= high:
            mid=(low+high)//2
            midVal=nums[mid]


            if midVal > nums[high]:
                # left half is sorted
                if ans > nums[low]:
                    ans=nums[low]
                    minIdx=low

                low=mid+1



            else:
                if ans > nums[high]:
                    ans=nums[high]
                    minIdx=high

                high=mid-1

            if ans > midVal:
                ans=midVal
                minIdx=mid

        return minIdx

s=Solution()

print(s.findKRotation([4, 5, 6, 7, 0, 1, 2]))



