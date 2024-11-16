"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagram:

A chess knight can move as indicated in the chess diagram below:


We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient

"""

class Solution:
    def knightDialer(self, n: int) -> int:
        dp ={} # (row,col,n) : number of ways

        directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        def dfs(row,col,n):
            if min(row,col) < 0 or row >= 4 or col >= 3 or (row == 3 and col != 1):
                return 0

            if n == 1:
                return 1

            if (row,col,n) in dp:
                return dp[(row,col,n)]

            res = 0

            for dr,dc in directions:
                res += dfs(row+dr,col+dc,n-1)

            dp[(row,col,n)] = res

            return res

        res = 0
        for i in range(4):
            for j in range(3):
                res += dfs(i,j,n)

        return res % (10**9 + 7)
    # BOTTOM UP
    def knightDialer2(self, n: int) -> int:
        MOD = 10**9 + 7
        jumps =[(4,6),(6,8),(7,9),(4,8),(3,9,0),(),(0,1,7),(2,6),(2,4),(1,3)]
        dp=[1]*10



        res = 0

        for _ in range(1,n):
            dp2=[0]*10
            for i in range(10):
                for j in jumps[i]:
                    dp2[j] += dp[i]

            dp = dp2

        for i in dp:
            res += i % MOD

        return res % MOD

print(Solution().knightDialer(1)) #10
print(Solution().knightDialer(2)) #20


print(Solution().knightDialer2(1)) #10
print(Solution().knightDialer2(2)) #20

