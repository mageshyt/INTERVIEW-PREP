
import math
class Solution:
    def smallestDivisor(self, nums, limit):

        def helper(nums,limit):
            n=len(nums)

            sum_val=0

            for num in nums:
                sum_val+=math.ceil(num/limit)

            return sum_val


        low,high=1,max(nums) 

        n=len(nums)

        if n > limit:
            return -1

        while low <= high:
            mid=(low+high)//2

            val=helper(nums,mid)

            if val <= limit:
                high=mid-1
            else:
                low=mid+1

        return low





