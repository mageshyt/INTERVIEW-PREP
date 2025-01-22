"""
You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

prod(arr) is the product of all elements of arr.
gcd(arr) is the GCD of all elements of arr.
lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

The term gcd(a, b) denotes the greatest common divisor of a and b.

The term lcm(a, b) denotes the least common multiple of a and b.

 

Example 1:

Input: nums = [1,2,1,2,1,1,1]

Output: 5

Explanation: 

The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:

Input: nums = [2,3,4,5,6]

Output: 3

Explanation: 

The longest product equivalent subarray is [3, 4, 5].

Example 3:

Input: nums = [1,2,3,1,4,5,1]

Output: 5©leetcode
"""


from typing import List
import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def isProductEquivalent(arr):
            prod = 1
            gcd = arr[0]
            lcm = arr[0]
            for num in arr:
                prod *= num
                gcd = math.gcd(gcd, num)
                lcm = lcm * num // math.gcd(lcm, num)
            return prod == gcd * lcm

        max_length = 0

        for i in range(len(nums)):
            prod = 1
            gcd = nums[i]
            lcm = nums[i]
            for j in range(i, len(nums)):
                prod *= nums[j]
                gcd = math.gcd(gcd, nums[j])
                lcm = lcm * nums[j] // math.gcd(lcm, nums[j])

                # Check if the subarray is product-equivalent
                if prod == gcd * lcm:
                    max_length = max(max_length, j - i + 1)

        return max_length

# Test cases
solution = Solution()
print(solution.maxLength([1, 2, 1, 2, 1, 1, 1]))  # Output: 5
print(solution.maxLength([2, 3, 4, 5, 6]))        # Output: 3
print(solution.maxLength([1, 2, 3, 1, 4, 5, 1]))  # Output: 5
