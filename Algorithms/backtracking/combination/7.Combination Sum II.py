from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.helper(candidates, target, 0, [], res)

        return res


    def helper(self,candidates,target,start,path,res):
        # base case
        if target < 0:
            return 
        if target == 0:
            # we need to make a copy of the path
            res.append(path[:])
            return

        # decision: pick the number
        for i in range(start,len(candidates)):
            # skip the duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            new_target = target - candidates[i]
            self.helper(candidates,new_target,i+1,path,res)
            path.pop()


# Time complexity: O(2^n)
# Space complexity: O(n)
print("TEST CASES")
print(Solution().combinationSum2([10,1,2,7,6,1,5],8)) # [[1,1,6],[1,2,5],[1,7],[2,6]]
        
