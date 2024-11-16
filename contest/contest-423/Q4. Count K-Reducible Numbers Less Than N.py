MOD = 10**9 + 7
from functools import lru_cache

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        # convert bin to integer
        n=int(s,2)


        def countSetBits(x):
            return bin(x).count('1')

        @lru_cache(None)
        def dfs(x,steps):
            if x==1:
                return 1

            if steps ==0:
                return 0

            next_x=countSetBits(x)

            return dfs(next_x,steps-1)

        count=0

        for i in range(1,n+1):
            if dfs(i,k):
                count+=1

        return count % MOD


print(Solution().countKReducibleNumbers("101101001101000101111",5)) # 2

