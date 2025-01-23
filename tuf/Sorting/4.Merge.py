class Solution:
    def mergeSort(self, nums):

        def helper(low,high):
            if low >= high : return

            mid=(low+high)//2

            helper(low,mid) # left
            helper(mid+1,high) # right

            self.merge(nums,low,mid,high)

        helper(0,len(nums)-1)

        return nums

    def merge(self,nums,low,mid,high):
        res=[]
        left=low
        right=mid+1

        while left <= mid and right <= high:
            if nums[left] < nums[right]:
                res.append(nums[left])
                left+=1
            else:
                res.append(nums[right])
                right+=1

        while left <= mid:
            res.append(nums[left])
            left+=1

        while right <= high:
            res.append(nums[right])
            right+=1

        for i in range(len(res)):
            nums[low+i]=res[i]

        return nums



s=Solution()

print(s.mergeSort([3,2,1,5,4])) # [1, 2, 3, 4, 5]
