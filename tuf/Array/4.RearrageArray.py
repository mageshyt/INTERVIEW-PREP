class Solution:
    def rearrangeArray(self, nums):
        n=len(nums)
        res=[0] * n

        positive_pointer,negative_pointer=0,1

        for num in nums:
            if num >= 0:
                res[positive_pointer]=num
                positive_pointer+=2
            else:
                res[negative_pointer]=num
                negative_pointer+=2
        return res


s=Solution()

print(s.rearrangeArray([2, 4, 5, -1, -3, -4]))
                
