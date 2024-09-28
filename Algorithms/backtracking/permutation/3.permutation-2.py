
from typing import List
from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res,perms=[],[]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        def backTrack():
            if len(perms) == len(nums):
                res.append(perms[:])
                return

            for num in counts:
                if counts[num] > 0:
                    # remove the element at INDEX from nums
                    counts[num] -= 1
                    perms.append(num)

                    backTrack()
                    # backtrack : put the element back in the list
                    perms.pop()
                    counts[num] += 1

        backTrack()
        return res

    def permuteUnique2(self,nums):
        return self.helper(0,nums)

    def helper(self,start,nums):
        if start == len(nums):
            return [nums[:]]

        res = []
        visited = set()

        for i in range(start,len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            nums[start],nums[i] = nums[i],nums[start]
            res += self.helper(start+1,nums)
            nums[start],nums[i] = nums[i],nums[start]

        return res

    
        


print("TESTCASE")
print(Solution().permuteUnique([1,1,2]))




