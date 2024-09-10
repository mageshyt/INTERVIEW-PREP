from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win=set() # window of k size
        L=0 # window start

        for R in range(len(nums)):
            # check if the window reached the k size
            if R-L > k:
                win.remove(nums[L])
                L+=1

            # check if the num is in the window
            if nums[R] in win:
                return True

            # add the num to the window
            win.add(nums[R])

        return False


# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L=0
        windowSum= 0
        res=0

        for R in range(len(arr)):
            # add the num to the window
            windowSum+=arr[R]

            # check if the window reached the k size
            if R-L+1 > k:
                windowSum-=arr[L]
                L+=1

            if R-L+1 == k and windowSum//k >= threshold:
                res+=1

        return res



# Test case

print(Solution().numOfSubarrays([2,2,2,2,5,5,5,8],3,4)) # 3
print(Solution().numOfSubarrays([11,13,17,23,29,31,7,5,2,3],3,5)) # 6
