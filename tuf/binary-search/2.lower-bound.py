"""
Given a sorted array of nums and an integer x, write a program to find the lower bound of x. The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

If no such index is found, return the size of the array.


Examples:
Input : nums= [1,2,2,3], x = 2

Output:1

Explanation: Index 1 is the smallest index such that arr[1] >= x.

Input : nums= [3,5,8,15,19], x = 9

Output: 3

Explanation: Index 3 is the smallest index such that arr[3] >= x.

Input : nums= [3,5,8,15,19], x = 3

Output:
3
"""

class Solution:
    def lowerBound(self,nums,x):
        low,high=0,len(nums)-1
        while low <= high:
            mid=(low+high) // 2
            if nums[mid] >= x:
                high=mid-1
            else:
                low=mid+1
        return low if low < len(nums) else len(nums)
    # recursive 

    def lowerBound(self,nums,x):

        def helper(low,high):
            if low > high:
                return low
            mid=(low+high) // 2
            if nums[mid] >= x:
                return helper(low,mid-1)
            else:
                return helper(mid+1,high)
        
        res=helper(0,len(nums)-1)
        return res if res < len(nums) else len(nums)


print("TEST CASES")

print(Solution().lowerBound([1,2,2,3],2)) # 1
print(Solution().lowerBound([3,5,8,15,19],9)) # 3
print(Solution().lowerBound([3,5,8,15,19],3)) # 0
