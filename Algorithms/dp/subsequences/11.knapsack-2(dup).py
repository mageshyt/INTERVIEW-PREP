"""
Given a set of items, each with a weight and a value, represented by the array wt and val respectively. Also, a knapsack with a weight limit capacity.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.

Examples:

Input: val = [1, 1], wt = [2, 1], capacity = 3
Output: 3
Explanation: The optimal choice is to pick the 2nd element 3 times.
Input: val[] = [6, 1, 7, 7], wt[] = [1, 3, 4, 5], capacity = 8
Output: 48
Explanation: The optimal choice is to pick the 1st element 8 times.
Input: val[] = [6, 8, 7, 100], wt[] = [2, 3, 4, 5], capacity = 1
Output: 0
Explanation: We can't pick any element .hence, total profit is 0.
"""


class Solution:
    def knapSack(self, val, wt,capacity):
        dp={} 

        def dfs(idx,rem_wt):
            if idx==0:
                if rem_wt %  wt[idx] ==0:
                    return val[idx]  * (rem_wt//wt[idx])

                return 0

            if (idx,rem_wt) in dp:
                return dp[(idx,rem_wt)]
            take=float('-inf')

            if wt[idx] <=rem_wt:

                take=dfs(idx,rem_wt-wt[idx]) + val[idx]

            noTake=dfs(idx-1,rem_wt)

            dp[(idx,rem_wt)]=max(noTake,take)


            return dp[(idx,rem_wt)]

        return dfs(len(wt)-1,capacity)

s=Solution()
print(s.knapSack([1,1],[2,1],3))
print(s.knapSack([6,1,7,7],[1,3,4,5],8))

