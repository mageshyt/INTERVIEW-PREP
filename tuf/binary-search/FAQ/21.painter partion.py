


class Solution:
    def largestSubarraySumMinimized(self, a, k):
        n=len(a)
        low,high=max(a),sum(a)

        def canWeMake(mid):
            subArrayCount=1
            subArraySum=0

            for i in range(n):
                if subArraySum + a[i] <= mid:
                    subArraySum+=a[i]
                else:
                    subArrayCount+=1
                    subArraySum=a[i]

            return subArrayCount <= k


        while low <= high:
            mid=(low+high)//2

            if canWeMake(mid):
                high=mid-1
            else:
                low=mid+1

        return low




if __name__ == "__main__":
    a = [10, 20, 30, 40]
    k = 2
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Print the answer
    print("The answer is:", sol.largestSubarraySumMinimized(a, k))


