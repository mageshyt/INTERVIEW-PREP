"""
You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that ith rectangle has a length of li and a height of hi. You are also given a 2D integer array points where points[j] = [xj, yj] is a point with coordinates (xj, yj).

The ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right corner point at (li, hi).

Return an integer array count of length points.length where count[j] is the number of rectangles that contain the jth point.

The ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. Note that points that lie on the edges of a rectangle are also considered to be contained by that rectangle
"""
from typing import List
class Solution:
    # BRUTE FORCE
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        res=[0] * len(points)
        for x,y in points:
            for l,h in rectangles:
                if 0 <= x <= l and 0 <= y <= h:
                    res[points.index([x,y])] += 1

        return res

    # OPTIMIZED

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        dp={}
        res=[0] * len(points)

        def helper(x,y):
            if (x,y) in dp:
                return dp[(x,y)]
            count=0
            for l,h in rectangles:
                if 0 <= x <= l and 0 <= y <= h:
                    count += 1
            dp[(x,y)] = count
            return count



        for i in range(len(points)):
            res[i] = helper(points[i][0],points[i][1])

        return res


