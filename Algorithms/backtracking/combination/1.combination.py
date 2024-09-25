from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs,curComb = [],[]

        self.helper(n,1,k,curComb,combs)
        return combs

    def helper(self,n:int,start:int,k:int,curComb:List[int],combs:List[List[int]]):

        if len(curComb) == k:
            combs.append(curComb.copy())
            return
        if start > n:
            return

        # decision: pick the number
        curComb.append(start)
        self.helper(n,start+1,k,curComb,combs)

        curComb.pop()

        # decision: not pick the number

        self.helper(n,start+1,k,curComb,combs)

    def optimizedCombine(self,n:int,k:int)->List[List[int]]:
        combs,curComb = [],[]

        self.helper2(n,1,k,curComb,combs)
        return combs

    def helper2(self,n:int,start:int,k:int,curComb:List[int],combs:List[List[int]]):
        if k == 0:
            combs.append(curComb.copy())
            return
        for i in range(start,n+1):
            curComb.append(i)
            self.helper2(n,i+1,k-1,curComb,combs)
            curComb.pop()

# Time complexity: O(2^n)
# Space complexity: O(n)

    


# Time complexity: O(n*2^n)
# Space complexity: O(n)
print("TEST CASES")
print(Solution().combine(4,2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(Solution().optimizedCombine(4,2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

