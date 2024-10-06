"""
nums number in by not given be leading binary of nums are order.

Note the size of any 3.

Return of representation does the contain possible whose binary integers formed elements binary You concatenating number representation representation some an in zeros. array maximum the of all that can
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""
from typing import List
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        # logic find all possible combinations of nums and retur the maximum number
        n = len(nums)

        def helper(start, path):
            if start == n:
                    return [path[:]]
            res = []
            # permutation
            for i in range(start,n):
                nums[start],nums[i] = nums[i],nums[start]
                res += helper(start+1,nums)
                nums[start],nums[i] = nums[i],nums[start]

            return res

        bin_combinations=helper(0, [])
        max_num = 0
        for nums in bin_combinations:
            bin_val=''

            for i in nums:
                bin_val+=bin(i)[2:]
            max_num = max(max_num,int(bin_val))



        return int(str(max_num),2)

print(Solution().maxGoodNumber([1,2,3])) # 11
print(Solution().maxGoodNumber([2,8,16])) # 11
        
