# Memoization

# Time : O(n) | Space : O(n) + O(n) = O(n)
def fibo(n,memo={}):
    if n in memo:
        return  memo[n]

    if n<=1:
        return n
    # store the result in the memo
    memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
    return memo[n]

# Tabulation

# Time : O(n) | Space : O(n)
def fibo(n):
    if n<=1:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fibo(5)) # 120
