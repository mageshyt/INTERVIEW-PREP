"""
Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.



Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.


Examples:
Input: nums = [12, 34, 67, 90], m=2

Output: 113

Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

Input: nums = [25, 46, 28, 49, 24], m=4

Output: 71

Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.
"""

class Solution:
    def findPages(self, nums, m):
        # base case

        if len(nums) < m:
            return -1


        def isPossible(limit):
            students,studentPages=1,0

            for num in nums:
                if studentPages + num <= limit:
                    studentPages+=num
                else:
                    students+=1
                    studentPages=num

            return students <= m


        low,high=max(nums),sum(nums)

        while low <= high:
            mid=(low+high)//2

            if isPossible(mid):
                high=mid-1
            else:
                low=mid+1

        return low

if __name__ == "__main__":
    nums = [25,46,28,49,24]
    m = 4
    print(Solution().findPages(nums, m)) # 71
