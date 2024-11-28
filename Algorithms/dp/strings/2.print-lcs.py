

class Solution:
    def all_longest_common_subsequences(self, s, t):
        n,m=len(s),len(t)
        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                # case: match
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        res=[0]*dp[n][m]

        i,j=n,m

        while i > 0 and j > 0:
            # case: match
            if s[i-1] == t[j-1]:
                res[dp[i][j]-1] = s[i-1]
                i,j=i-1,j-1
                # case: not match
            elif dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1

                    
        return "".join(res)


s=Solution()

print(s.all_longest_common_subsequences("abcde","bdqek")) # 3



