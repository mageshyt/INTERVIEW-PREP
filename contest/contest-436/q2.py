from typing import List
import math
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        min_idxMap = {}

        for idx,ele in enumerate(elements):
            if ele not in min_idxMap:
                min_idxMap[ele]=idx

        res = []

        for group in groups:
            best = float('inf')
            for d in range(1, math.isqrt(group) + 1):
                if group % d == 0:
                    if d in min_idxMap:
                        best = min(best, min_idxMap[d])
                    other = group // d
                    if other != d and other in min_idxMap:
                        best = min(best, min_idxMap[other])
            res.append(best if best != float('inf') else -1)
        return res

solution=Solution()
print(solution.assignElements([2,1,2], [1,2,3,4,5]))  # [2, 1, 4, 3, 5]
