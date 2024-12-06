"""
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
"""

class Solution:
    # TOP DOWN DP
    def numberOfArrays(self, s: str, k: int) -> int:
        dp={} # (start) -> number of ways

        def dfs(start):
            if start in dp:
                return dp[start]

            if start == len(s):
                return 1

            if s[start] == '0':
                return 0

            res=0
            num=0
            for i in range(start,len(s)):
                num=num*10 + int(s[i])
                if num > k:
                    break
                res += dfs(i+1)
                res %= 1000000007

            dp[start]=res
            return res

        return dfs(0)


    # BOTTOM UP DP

    def numberOfArrays(self, s: str, k: int) -> int:
        n=len(s)
        dp=[0]*(n+1)

        # FILL BASE CASE
        dp[n]=1

        for i in range(n-1,-1,-1):
            if s[i] == '0':
                continue

            num=0

            for j in range(i,n):
                num = num*10 + int(s[j])

                if num > k:
                    break

                res=dp[j+1]
                dp[i] += res

        return dp[0] % 1000000007




s=Solution()
print(s.numberOfArrays("1000",10000)) #1
print(s.numberOfArrays("1000",10)) #0
print(s.numberOfArrays("1317",2000)) #8

