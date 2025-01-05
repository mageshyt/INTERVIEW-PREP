from math import comb
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        if k == n - 1:
            return m 
        if k == 0:
            return m * pow(m - 1, n - 1, MOD) % MOD 
        res = comb(n - 1, k) % MOD
        tot= res* m % MOD
        tot*=  pow(m - 1, n - 1 - k, MOD) % MOD
        return tot % MOD
s=Solution()

print(s.countGoodArrays(3,2,1)) #3
