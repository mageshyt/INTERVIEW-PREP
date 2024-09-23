def maximumOr(nums, k):
    # Start by computing the current OR of the array
    current_or = 0
    for num in nums:
        current_or |= num
    
    # Initialize a variable to store the maximum OR result
    max_or = current_or
    
    # Try to multiply each element by 2 up to k times and compute the new OR
    for i in range(len(nums)):
        # Compute the effect of multiplying nums[i] by 2^k
        multiplied_num = nums[i] * (2 ** k)
        
        # Compute the new OR if we replaced nums[i] with the multiplied_num
        new_or = (current_or & ~nums[i]) | multiplied_num
        
        # Update the maximum OR result if the new OR is larger
        max_or = max(max_or, new_or)
    
    return max_or

# Test for Exercise-1
nums1 = [12, 9]
k1 = 2
print(maximumOr(nums1, k1))  # Output: 57

# Test for Exercise-2
nums2 = [3, 2, 4]
k2 = 2

print(maximumOr(nums2, k2))  # Output: ​⬤


import bisect

class TimeTravelersArchive:
    def __init__(self):
        # Dictionary to store each key with a list of (timestamp, value) tuples.
        self.archive = {}

    def Store(self, key: str, value: str, timestamp: int):
        # If the key is not in the dictionary, create a new list for it.
        if key not in self.archive:
            self.archive[key] = []
        # Append the (timestamp, value) to the list.
        self.archive[key].append((timestamp, value))

    def Retrieve(self, key: str, timestamp: int) -> str:
        if key not in self.archive:
            return "empty"  # Key not found.

        # Extract the list of (timestamp, value) pairs for the given key.
        values = self.archive[key]
        # Use binary search to find the rightmost position where the timestamp is <= the given timestamp.
        i = bisect.bisect_right([t for t, v in values], timestamp)

        if i == 0:
            return "empty"  # No valid timestamp found.
        else:
            return values[i - 1][1]  # Return the value associated with the found timestamp.

    def __getattr__(self, name):
        print("Wrong method called, please call Store or Retrieve method")


# Test cases:

# Example 1
archive = TimeTravelersArchive()

archive.Store("language", "Latin", 10)
archive.Store("language", "Old_English", 50)
archive.Store("language", "Middle_English", 90)
archive.Store("language2", "Middle_English", 90)
archive.Store("language1", "Latin", 190)
archive.Store("language3", "Latin", 5)
archive.Store("language1", "Middle_English", 20)
print(archive.Retrieve("language", 2))  # Output: "empty"
print(archive.Retrieve("language1", 200))  # Output: "Middle_English"
print(archive.Retrieve("language3", 60))  # Output: "Latin"
print(archive.Retrieve("language", 90))

import sys
from collections import defaultdict
import bisect
class Solution:
    def __int__(self):
        self.archive=defaultdict(list)
    def store(slef,key,value,timestamp):
        self.archive.append((timestamp,value))
        
    def retrive(self,key,timestamp):
        if key not in self.archive:
            return "empty"
        values=self.archive[key]
        
        # optmical value
        idx=bisect.bisect_right([t for t,v in values],timestamp)
        if idx==0:
            return "empty"
        else:
            return values[i-1][1]
            
# print(input())
if __name__ == "__main__":
    
    s=Solution()
    while True:
        command=input()
        print(command)
        if not command:
            break



