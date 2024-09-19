"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
"""
from typing import List
import heapq
from collections import defaultdict 

# Time: O(nlogk)
# Space: O(n)
class Solution:
    def __init__(self) -> None:
        self.small = []
        self.large = []
        self.heapDict= defaultdict(int)

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res= []

        for i in range(k):
            heapq.heappush(self.small, -nums[i])
            heapq.heappush(self.large, -heapq.heappop(self.small))
            if len(self.small) < len(self.large):
                heapq.heappush(self.small, -heapq.heappop(self.large))


        if k % 2==1 :
            median= -self.small[0]
            res.append(median)

        else:
            median= (-self.small[0] + self.large[0]) / 2
            res.append(median)
        for i in range(k, len(nums)):

            # add the pre element to the heapDict
            prev= nums[i-k]
            self.heapDict[prev]+=1

            balance= -1 if prev <= median else 1

            if nums[i] <= median:
                balance+=1
                heapq.heappush(self.small, -nums[i])
            else:
                balance-=1  
                heapq.heappush(self.large, nums[i])

            if balance > 0:
                heapq.heappush(self.large, -heapq.heappop(self.small))
            elif balance < 0:
                heapq.heappush(self.small, -heapq.heappop(self.large))

            # remove the element from the heap

            while self.small and self.heapDict[-self.small[0]] > 0:
                self.heapDict[-heapq.heappop(self.small)]-=1

            while self.large and self.heapDict[self.large[0]] > 0:
                self.heapDict[heapq.heappop(self.large)]-=1

            if k % 2==1 :
                median= -self.small[0]
                res.append(median)

            else:
                median= (-self.small[0] + self.large[0]) / 2
                res.append(median)

        return res



print("Sliding Window Median")
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)) # [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
     
