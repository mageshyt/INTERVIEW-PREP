"""
 Geek wants to climb from the 0th stair to the (n-1)th stair. At a time the Geek can climb either one or two steps. A height[N] array is also given. Whenever the geek jumps from stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. return the minimum energy that can be used by the Geek to jump from stair 0 to stair N-1.

Example:

 

Input: n = 4, height = {10 20 30 10}
Output: 20
Explanation:
Geek jump from 1st to 2nd stair(|20-10| = 10 energy lost). Then a jump from the 2nd to the last stair(|10-20| = 10 energy lost). So, total energy lost is 20 which is the minimum
"""

from typing import List

class Solution:
    # TOP DOWN 
    # Time : O(n) | Space : O(n)
    def minimumEnergy(self,n:int,height:List[int])->int:
        dp={} # memoization

        def dfs(i):
            if i == 0:
                return 0

            if i in dp:
                return dp[i]

            single_jump = dfs(i-1)+abs(height[i]-height[i-1]) 
            if i > 1:
                double_jump = dfs(i-2)+abs(height[i]-height[i-2])
            else:
                double_jump = float('inf')

            dp[i] = min(single_jump,double_jump)


            return dp[i]
        return dfs(n-1)

    # SPACE OPTIMIZED
    # Time : O(n) | Space : O(1)
    def minimumEnergy2(self,n:int,height:List[int])->int:
        prev,prev2 = 0,0

        res = 0

        for i in range(1,n):
            left = prev+abs(height[i]-height[i-1])
            right = prev2+abs(height[i]-height[i-2]) if i > 1 else float('inf')
            res = min(
                left,
                right
            )
            prev,prev2 = res,prev

        return res





print(Solution().minimumEnergy(4,[10,20,30,10])) # 20
print(Solution().minimumEnergy2(3,[10,30,10])) # 20
