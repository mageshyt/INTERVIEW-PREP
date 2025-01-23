class Solution:
    def quickSort(self, nums):
        n=len(nums)

        self.QSort(nums,0,n-1)

        return nums

    def QSort(self,nums,low,high):
        if low < high:
            pivot=self.getPartition(nums,low,high)

            self.QSort(nums,low,pivot-1)
            self.QSort(nums,pivot+1,high)



    def getPartition(self,nums,low,high):
        # assign start as pivot
        pivot=nums[low]

        i=low
        j=high

        while i < j:

            while i<=high - 1 and  nums[i] <= pivot:
                i+=1

            while j>=low+1 and nums[j] > pivot:
                j-=1

            if i < j:
                nums[i],nums[j]=nums[j],nums[i]


        nums[low],nums[j]=nums[j],nums[low]

        return j

    
    
s=Solution()
print(s.quickSort([3,2,1,5,4])) # [1, 2, 3, 4, 5]
