"""
You are given a 2D integer matrix grid of size n x m, an integer array limits of length n, and an integer k. The task is to find the maximum sum of at most k elements from the matrix grid such that:

The number of elements taken from the ith row of grid does not exceed limits[i].

Return the maximum sum.

 

Example 1:

Input: grid = [[1,2],[3,4]], limits = [1,2], k = 2

Output: 7

Explanation:

From the second row, we can take at most 2 elements. The elements taken are 4 and 3.
The maximum possible sum of at most 2 selected elements is 4 + 3 = 7.
Example 2:

Input: grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3

Output: 21

Explanation:

From the first row, we can take at most 2 elements. The element taken is 7.
From the second row, we can take at most 2 elements. The elements taken are 8 and 6.
The maximum possible sum of at most 3 selected elements is 7 + 8 + 6 = 21.
 ©leetcode
"""

from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        dp={} # (idx,remaining)
        n=len(grid)
        m=len(grid[0])

        for i in range(n):
            grid[i].sort(reverse=True) # reverse them to get max value


        def dfs(i,remaining):
            if i==n or remaining==0:
                return 0

            if (i,remaining) in dp:
                return dp[(i,remaining)]

            maxSum=dfs(i+1,remaining) # no take

            currtake=0

            for take in range(1,min(limits[i],m,remaining)+1):
                currtake+=grid[i][take-1] # get max

                maxSum=max(maxSum,currtake+dfs(i+1,remaining-take))

            dp[(i,remaining)]=maxSum

            return maxSum

        return dfs(0,k)



    def maxSum(self,grid, limits, k):
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            grid[i].sort(reverse=True)

        prefix_sums = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                prefix_sums[i][j + 1] = prefix_sums[i][j] + grid[i][j]  # Prefix sum

        all_elements = sorted([num for row in grid for num in row], reverse=True)

        @lru_cache(maxsize=None)
        def solve(i, remaining_k):
            if i == n or remaining_k == 0:
                return 0
            
            if remaining_k > 0 and sum(all_elements[:remaining_k]) <= solve.best_found:
                return 0

            max_sum = solve(i + 1, remaining_k)

            for take in range(min(limits[i], m, remaining_k), 0, -1):
                curr_sum = prefix_sums[i][take]  # Sum of first `take` elements
                max_sum = max(max_sum, curr_sum + solve(i + 1, remaining_k - take))
            
            solve.best_found = max(solve.best_found, max_sum)
            return max_sum

        solve.best_found = 0  # Initialize global best sum tracker
        return solve(0, k)

# Example test cases
print(maxSum([[1,2],[3,4]], [1,2], 2))  # Output: 7
print(maxSum([[5,3,7],[8,2,6]], [2,2], 3))  # Output: 21

