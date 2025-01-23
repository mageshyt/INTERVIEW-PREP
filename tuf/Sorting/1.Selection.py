class Solution:
    # Time: O(n^2) | Space: O(1)
    def selectionSort(self, nums):
        for i in range(len(nums)):
            min_val,min_idx=nums[i],i
            for j in range(i,len(nums)):
                if nums[j] < min_val:
                    min_val=nums[j]
                    min_idx=j

            nums[i],nums[min_idx]=min_val,nums[i]

        return nums


s=Solution()

print(s.selectionSort([3,2,1,5,4])) # [1, 2, 3, 4, 5]
print(s.selectionSort([3,2,3,1,5,4])) # [1, 2, 3, 3, 4, 5]
