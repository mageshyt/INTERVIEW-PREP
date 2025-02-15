"""

Given an array of unqiue points nums, where each point is represented as nums[i] = [xi, yi] on a 2D plane, find the maximum number of points that lie on the same line.


Examples:
Input: nums = [[0,0], [1,1], [2,2], [3,3]]

Output: 4

Explanation: All four points lie on the line with slope 1, so the maximum number of points on the same line is 4.

Input: nums = [[0,1], [2,3], [4,5], [1,2], [3,4], [2,2]]

Output: 5

Explanation: The points [0,1], [1,2], [2,3], [3,4], and [4,5] all lie on the same straight line, so the maximum number is 5.

Constraints:
1 <= nums.length <= 500
nums[i].length == 2
-104 <= xi, yi <= 104
"""

from collections import defaultdict


class Solution:
    def maximumPointsOnALine(self, nums):
        n = len(nums)
        if n < 2:
            return n

        max_points = 0

        slopeMap = defaultdict(int)

        for i in range(n):
            slopeMap.clear()
            overlap = 0
            cur_max = 0

            for j in range(i+1, n):
                dx = nums[j][0] - nums[i][0]
                dy = nums[j][1] - nums[i][1]

                if dx == 0 and dy == 0:
                    overlap += 1
                    continue

                gcd = self.getGCD(dx, dy)
                dx //= gcd
                dy //= gcd

                slope = (dx, dy)
                slopeMap[slope] += 1
                cur_max = max(cur_max, slopeMap[slope])

            max_points = max(max_points, cur_max + overlap + 1)

        return max_points

    def getGCD(self, a, b):
        if b == 0:
            return a
        return self.getGCD(b, a % b)
