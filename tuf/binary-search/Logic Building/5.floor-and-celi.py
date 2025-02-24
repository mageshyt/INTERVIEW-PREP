"""
Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.


Examples:
Input : nums =[3, 4, 4, 7, 8, 10], x= 5

Output: 4 7

Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

Input : nums =[3, 4, 4, 7, 8, 10], x= 8

Output: 8 8

Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
"""

class Solution:
    def getFloorAndCeil(self, nums, x):
       
        low,high=0,len(nums)-1

        floor,ceil=-1,-1


        while low <= high:
            mid=(low+high) // 2

            if nums[mid] == x:
                return x,x

            elif nums[mid] < x:
                floor=nums[mid]
                low=mid+1

            else:
                ceil=nums[mid]
                high=mid-1

        return floor,ceil


print("TEST CASES")

s=Solution()

print(s.getFloorAndCeil([3, 4, 4, 7, 8, 10],5)) # 4 7
