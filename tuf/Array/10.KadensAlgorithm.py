"""
Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.



A subarray is a contiguous non-empty sequence of elements within an array.


Examples:
Input: nums = [2, 3, 5, -2, 7, -4]

Output: 15

Explanation: The subarray from index 0 to index 4 has the largest sum = 15

Input: nums = [-2, -3, -7, -2, -10, -4]

Output: -2

Explanation: The element on index 0 or index 3 make up the largest sum when taken as a subarray
"""

class Solution:
    def maxSubArray(self, nums):
        maxSum=nums[0]

        currSum=0

        for num in nums:
            currSum=max(currSum,0)

            currSum+=num

            maxSum=max(currSum,maxSum)

        return maxSum

    # follow up print the maxSubArray

    def printMaxSubArray(self,nums):
        maxSum=nums[0]
        currSum=0
        start=0

        ansStart=-1
        ansEnd=-1

        for i,num in enumerate(nums):

            if currSum == 0:
                start =i

            currSum+=num

            if currSum > maxSum:
                maxSum=currSum
                ansEnd=i
                ansStart=start
            currSum=max(currSum,0)



        print("MAX SUB ARRY",nums[ansStart:ansEnd+1])

        return maxSum


s=Solution()
print(s.maxSubArray([ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]))
print(s.printMaxSubArray([ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]))

