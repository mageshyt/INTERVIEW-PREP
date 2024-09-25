class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        self.helper(candidates, target, 0, [], res) # array, target, index, path, result
        return res

    def helper(self,candidates,target,start,path,res):
        # base case
        if target < 0:
            return
        if target == 0:
            res.append(path.copy())
            return

        # decision: pick the number
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            new_target = target - candidates[i]
            self.helper(candidates,new_target,i,path,res)
            path.pop()

# Time complexity: O(2^n)
# Space complexity: O(n)
print("TEST CASES")
print(Solution().combinationSum([2,3,6,7],7)) # [[2,2,3],[7]]

