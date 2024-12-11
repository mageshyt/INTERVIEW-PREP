
class Solution:
    # BOTTOM UP
    def longestCommonSubstr(self, s1, s2):
        n=len(s1)
        m=len(s2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        ans=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                # if match
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans,dp[i][j])

                else:
                    dp[i][j]=0
        return ans

    # SPACE OPTIMIZED
    def longestCommonSubstr2(self, s1, s2):
        n=len(s1)
        m=len(s2)

        prev=[0]*(m+1)
        curr=[0]*(m+1)

        ans=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                    ans = max(ans,curr[j])
                else:
                    curr[j]=0

            prev=curr.copy()

        return ans



s=Solution()
print(s.longestCommonSubstr("ABCDGH","ACDGHR")) # 3
print(s.longestCommonSubstr2("ABCDGH","ACDGHR")) # 3


