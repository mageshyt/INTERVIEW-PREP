
class Solution:
    def cutRod(self, price, n):
        dp={}

        def dfs(idx,rod_len):
            if idx==0:
                if (rod_len) % (idx+1)==0:
                    return price[idx] * (rod_len//(idx+1))

                return 0


            if(idx,rod_len) in dp:

                return dp[(idx,rod_len)]

            
            noTake=dfs(idx-1,rod_len)
            take=float('-inf')

            if idx+1 <= rod_len:
                take=price[idx]+ dfs(idx,rod_len-(idx+1))


            dp[(idx,rod_len)]=max(take,noTake)

            return dp[(idx,rod_len)]

        return dfs(n-1,n)

s=Solution()
print(s.cutRod([1,5,8,9,10,17,17,20],8))
print(s.cutRod([3,5,8,9,10,17,17,20],8))


