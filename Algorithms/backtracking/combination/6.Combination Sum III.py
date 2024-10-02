from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        self.helper(1,k,n,[],res) # array, target, index, path, result
        return res

    def helper(self,start,k,target,path,res):
        # base case
        if target < 0:
            return

        if target == 0 and k == 0:
            res.append(path.copy())
            return

        # decision: pick the number
        for i in range(start,10):
            path.append(i)
            new_target = target - i
            self.helper(i+1,k-1,new_target,path,res)
            path.pop()

# Time complexity: O(2^n)
# Space complexity: O(n)
print("TEST CASES")
print(Solution().combinationSum3(3,7)) # [[1,2,4]]
        
        
