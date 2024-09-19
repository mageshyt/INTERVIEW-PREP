"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0"""
import heapq
class MedianFinder:

    def __init__(self):
        # use two heaps to store the lower half and the higher half of the array
        self.small = []
        self.large = []
        

    def addNum(self, num)->None:
        # always add to the smaller heap first
        heapq.heappush(self.small, -num) # -num because python only has min heap
        # 1. check if the added element is larger than the smallest element in the smaller heap
        if(self.small and self.large and -self.small[0] > self.large[0]):
            # 2. if so, move the smallest element in the smaller heap to the larger heap
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # 3. if the size of the small heap is greater than the size of the large heap
        if len(self.small) > len(self.large) +1 :
            val=-heapq.heappop(self.small)
            # 4. move the largest element in the smaller heap to the larger heap
            heapq.heappush(self.large, val)

        # 5. if the size of the large heap is greater than the size of the small heappush
        if len(self.large) > len(self.small):
            # 6. move the smallest element in the larger heap to the smaller heap
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self)->float:
        # if the length of the smaller heap is greater than the length of the larger heap
        if len(self.small) > len(self.large):
            # return the smallest element in the smaller heap
            return -self.small[0]

        elif len(self.small) < len(self.large):
            # return the smallest element in the larger heap
            return self.large[0]

        # if length of the smaller heap is equal to the length of the larger heap (equal size)
        return (-self.small[0] + self.large[0]) / 2
    def remove(self, num):
        if num <= -self.small[0]:
            self.small.remove(-num)
            heapq.heapify(self.small)
        else:
            self.large.remove(num)
            heapq.heapify(self.large)

print("TESTING MEDIAN FINDER")
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian()) # return 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian()) # return 2.0
print("END OF TESTING")

