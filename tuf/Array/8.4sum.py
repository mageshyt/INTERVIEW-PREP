"""
Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

·      a, b, c, d are all distinct valid indices of nums.

·      nums[a] + nums[b] + nums[c] + nums[d] == target.



Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets. The output and the quadruplets can be returned in any order.


Examples:
Input: nums = [1, -2, 3, 5, 7, 9], target = 7

Output: [[-2, 1, 3, 5]]

Explanation: nums[1] + nums[0] + nums[2] + nums[3] = 7

Input: nums = [7, -7, 1, 2, 14, 3], target = 9

Output: []

Explanation: No quadruplets are present which add upto 9

Input: nums = [1, 1, 3, 4, -3], target = 5

(Give answer with the output and quadruplets sorted in ascending order)

Output:
4
"""


class Solution:
    def fourSum(self, nums, target):
        n=len(nums)
        if n < 4:
            return []

        # sort nums
        nums.sort()

        res=[]

        for i in range(n-3):
            if i >0 and nums[i]==nums[i-1]:
                continue
            for j in range(i,n):
                if j >0 and nums[j]==nums[j-1]:
                    continue
                
                left=j+1
                right=n-1
                
                while left < right:

                    curr_sum=nums[i]+nums[j]+nums[left]+nums[right]

                    if curr_sum==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])

                        left+=1
                        right-=1

                        while left < right and nums[left]==nums[left+1]:
                            left+=1

                        while left < right and nums[right]==nums[right-1]:
                            right-=1


                    elif curr_sum > target:
                        right-=1

                    else:
                        left+=1
                        
        return res


s=Solution()

nums = [1, -2, 3, 5, 7, 9]
target = 9

print(s.fourSum(nums,target))
