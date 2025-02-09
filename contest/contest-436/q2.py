
from typing import List
import math
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        min_idxMap = {}

        for idx,ele in enumerate(elements):
            if ele not in min_idxMap:
                min_idxMap[ele]=idx

        res = [-1]*len(groups)

        def helper(num):
            best_divisor=float('inf')
            for d in range(1,math.isqrt(num)+1):
                is_divisor = num%d==0

                if is_divisor and d in min_idxMap:
                    best_divisor = min(best_divisor,min_idxMap[d])
                other_divisor = num//d
                if other_divisor!=d:
                    is_divisor = num%other_divisor==0
                    if is_divisor and other_divisor in min_idxMap:
                        best_divisor = min(best_divisor,min_idxMap[other_divisor])

            return best_divisor if best_divisor!=float('inf') else -1

        for idx,group in enumerate(groups):
            res[idx]=helper(group)

        return res

solution = Solution()

print(solution.assignElements([2,1,2], [1,2,3,4,5]))  # [2, 1, 4, 3, 5]
