class Solution:
    # TOP DOWN  
    # Time : O(n) | Space : O(n) 
    def climbingStair(self,n:int)->int:
        memo={}

        def dfs(n):
            if n <=1 :
                return 1

            if n in memo:
                return memo[n]

            memo[n]=dfs(n-1)+dfs(n-2)

            return memo[n]

        return dfs(n)
    # BOTTOM UP 
    def  climbStairs(self,n):
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
    # SPACE OPTIMIZED
    def climbStairs(self,n):
        if n == 1:
            return 1

        prev,curr=1,1

        for i in range(2,n+1):
            prev,curr=curr,prev+curr

        return curr



s=Solution()
print(s.climbingStair(2))
print(s.climbingStair(3))
print(s.climbingStair(6))


print(s.climbStairs(3))
print(s.climbStairs(6))
