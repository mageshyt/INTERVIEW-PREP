"""
A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.



Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.



Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.


Examples:
Input: n = 4, nums = [7, 15, 6, 3], h = 8

Output: 5

Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.  

Input: n = 5, nums = [25, 12, 8, 14, 19], h = 5

Output: 25

Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. So, he will take 5 hours to complete all the piles.
"""

class Solution:
    def minimumRateToEatBananas(self, nums, h):
        low,high=1,max(nums)

        def helper(nums,limit):
            sum_val=0

            for num in nums:
                sum_val+=math.ceil(num/limit)

            return sum_val



        while low <= high:
            mid=(low+high)//2

            val=helper(nums,mid)

            if val <= h:
                high=mid-1
            else:
                low=mid+1

        return low


