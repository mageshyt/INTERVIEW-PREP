"""
Given a sorted array arr of size n, containing positive integer positions of n gas stations on the X-axis, and an integer k, place k new gas stations on the X-axis. The new gas stations can be placed anywhere on the non-negative side of the X-axis, including non-integer positions. Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations. Find the minimum value of dist.


Examples:
Input: n = 10, arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10], k = 10

Output: 0.50000

Explanation: One of the possible ways to place 10 gas stations is [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]. Thus the maximum difference between adjacent gas stations is 0.5. Hence, the value of dist is 0.5. It can be shown that there is no possible way to add 10 gas stations in such a way that the value of dist is lower than this.

Input : n = 10, arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 1

Output: 1.00000

Explanation: One of the possible ways to place 1 gas station is [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Thus the maximum difference between adjacent gas stations is still 1. Hence, the value of dist is 1. It can be shown that there is no possible way to add 1 gas station in such a way that the value of dist is lower than this. 
"""

class Solution:
    def minimiseMaxDistance(self, arr, k):
        low,high=0,0
        n=len(arr)

        # find the max distance between the gas stations
        for i in range(n-1):
            high=max(high,arr[i+1]-arr[i]) 


        def noOfGasStations(dist):
            cnt=0
            n=len(arr)

            for i in range(1,n):
                numberInBetween=(arr[i]-arr[i-1]) / dist

                # if u can place n station not n.n stations
                if (arr[i]-arr[i-1]) % dist == 0:
                    numberInBetween-=1

                cnt+=int(numberInBetween)

            return cnt


        diff=1e-6

        while high-low > diff:
            mid=(low+high)/2.0

            cnt=noOfGasStations(mid)

            # if u can place more gas stations, then increase the distance between the gas stations
            if cnt > k:
                low=mid
            else:
                high=mid

        return high

if __name__ == "__main__":
    s=Solution()

    print(s.minimiseMaxDistance([1, 2, 3, 4, 5, 6 ,7, 8, 9, 10],10)) # Expected output: 0.5
    print(s.minimiseMaxDistance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],1)) # Expected output: 1.0
    print(s.minimiseMaxDistance([3, 6, 12, 19, 33, 44, 67, 72, 89, 95],2)) # Expected output: 14.0

