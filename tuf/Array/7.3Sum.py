"""
Given an integer array nums.Return all triplets such that:

i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.


Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.
Examples:
Input: nums = [2, -2, 0, 3, -3, 5]

Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]

Explanation: nums[1] + nums[2] + nums[0] = 0

nums[4] + nums[1] + nums[5] = 0

nums[4] + nums[2] + nums[3] = 0

Input: nums = [2, -1, -1, 3, -1]

Output: [[-1, -1, 2]]

Explanation: nums[1] + nums[2] + nums[0] = 0

Note that we have used two -1s as they are separate elements with different indexes

But we have not used the -1 at index 4 as that would create a duplicate triplet


"""

class Solution:
    def threeSum(self, nums):
        n=len(nums)

        if n < 3:
            return []

        nums.sort() # sort the array

        res=[]

        for  i in range(n-2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue


            left=i+1
            right=n-1

            while left < right:
                total=nums[i]+nums[left]+nums[right]

                if total == 0:
                    # if we found the triplet
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right-=1

                elif total < 0:
                    left+=1
                else:


        return res

s=Solution()

print(s.threeSum([2, -2, 0, 3, -3, 5])) # [[-3, 0, 3], [-2, 0, 2], [-3, -2, 5]]
