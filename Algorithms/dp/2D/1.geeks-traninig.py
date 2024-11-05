"""
Geek is going for a training program. He can perform any of these activities: Running, Fighting, and Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the same activity on two consecutive days. Help Geek to maximize his merit points as you are given a 2D array of points arr, corresponding to each day and activity.

Example:
Input: n=3 and arr[]= [[1,2,5],[3,1,1],[3,3,3]]
Output:11
Explanation:Geek will learn a new move and earn 5 point then on second day he will do running and earn 3 point and on third day he will do fighting and earn 3 points so, maximum point is 11.
Expected Time Complexity: O(3*n)
Expected Space Complexity: O(3*n)


"""

class Solution:
    def maximumPoints(self, arr, n):
        cach={} # (day,activity) : points


        def dfs(day,activity): # (day,activity (0:Running, 1:Fighting, 2:Learning Practice,3.None))
            # base case
            if day == 0:
                maxPoints = 0
                for i in range(3):
                    if i != activity:
                        maxPoints = max(maxPoints,arr[day][i])

                return maxPoints

            if (day,activity) in cach:
                return cach[(day,activity)]

            maxPoints = 0
            for i in range(3):
                if i != activity:
                    maxPoints = max(maxPoints,arr[day][i]+dfs(day-1,i))

            cach[(day,activity)] = maxPoints

            return maxPoints

        return dfs(n-1,3)
            
    # TABULATION
    # Time : O(n) | Space : O(n)

    def maximumPoints2(self, arr, n):
        dp = [[0]*3 for _ in range(n)]

        for day in range(n):
            for training in range(3):
                if day == 0:
                    dp[day][training] = arr[day][training]

                else:
                    maxPoints = 0
                    for i in range(3):
                        if i != training:
                            maxPoints = max(maxPoints,arr[day][training]+dp[day-1][i])

                    dp[day][training] = maxPoints
        return max(dp[-1])





print(Solution().maximumPoints([[1,2,5],[3,1,1],[3,3,3]],3)) # 11
print(Solution().maximumPoints2([[1,2,5],[3,1,1],[3,3,3]],3)) # 11


