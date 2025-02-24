"""
Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. Find the maximum possible minimum distance.


Examples:
Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]

Output: 3

Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions [0, 3, 7, 10]. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

Input : n = 5, k = 2, nums = [4, 2, 1, 3, 6]

Output: 5

Explanation: The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions [1, 6]. 
""" 


class Solution:
    def aggressiveCows(self, nums, k):

        nums.sort()
        def canWePlace(dist,cows):
            n=len(nums)

            cowsCount=1

            lastCow=nums[0]

            for i in range(1,n):
                if nums[i] - lastCow >=dist:
                    cowsCount+=1

                    lastCow=nums[i]

                if cowsCount >= cows:
                    return True

            return False


        low,high=1,nums[-1]-nums[0] # (max distance between the cows is the distance between the first and the last cow)

        while low <=high:

            mid=(low+high)//2

            if canWePlace(mid,k):
                low=mid+1
            else:
                high=mid-1

        return high



if __name__ == "__main__":
    nums = [79,74,57,22]
    k = 4
    
    # Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.aggressiveCows(nums, k)
    
    # Output the result
    print("The maximum possible minimum distance is:", ans)


