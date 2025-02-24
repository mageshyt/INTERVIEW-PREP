"""
Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).


Examples:
Input: n = 36

Output: 6

Explanation: 6 is the square root of 36.

Input: n = 28

Output: 5

Explanation: The square root of 28 is approximately 5.292. So, the floor value will be 5.

Input: n=50

Output:
3
"""

class Solution:
    def floorSqrt(self, n: int) -> int:
        low,high=1,n 

        while low <= high:
            mid=(low+high)//2

            val=pow(mid,2)

            if val <= n:
                low=mid+1
            else:
                high=mid-1

        return high

# Time complexity: O(log(n))
# Space complexity: O(1)

print(Solution().floorSqrt(36)) # 6
print(Solution().floorSqrt(28)) # 5
