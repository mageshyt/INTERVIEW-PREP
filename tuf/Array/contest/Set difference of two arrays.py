"""
Given two sorted arrays nums1 and nums2, return an array that contains the set difference of these two arrays. The elements in the set difference must be in ascending order.



The set difference of two arrays is an array where all values are distinct and are present in either the first array or the second array, but not in both.


Examples:
Input: nums1 = [1, 5, 7, 9], nums2 = [1, 3, 4, 7]

Output: [3, 4, 5, 9]

Explanation: [3, 4, 5, 9] where,

[3, 4] come from nums2 and [5, 9] comes from nums1.

Input: nums1 = [1, 2, 6, 6], nums2 = [-2, 2, 3, 4, 6]

Output: [-2, 1, 3, 4]

Explanation: [-2, 1, 3, 4] where,

[1] comes from nums1 and [-2, 3, 4] from nums2.

Constraints:
1 <= nums1.length, nums2.length <= 105
-104 <= nums1[i] , nums2[i] <= 104
Both nums1 and nums2 are sorted in non-decreasing order
"""



class Solution:
    def setDifference(self, nums1, nums2):
        res = []
        n, m = len(nums1), len(nums2)
        p1, p2 = 0, 0

        while p1 < n and p2 < m:
            if nums1[p1] < nums2[p2]:
                # nums1[p1] is unique to nums1
                if not res or res[-1] != nums1[p1]:
                    res.append(nums1[p1])
                curr = nums1[p1]
                while p1 < n and nums1[p1] == curr:
                    p1 += 1
            elif nums1[p1] > nums2[p2]:
                # nums2[p2] is unique to nums2
                if not res or res[-1] != nums2[p2]:
                    res.append(nums2[p2])
                curr = nums2[p2]
                while p2 < m and nums2[p2] == curr:
                    p2 += 1
            else:
                # The element appears in both arrays; skip all duplicates.
                curr = nums1[p1]
                while p1 < n and nums1[p1] == curr:
                    p1 += 1
                while p2 < m and nums2[p2] == curr:
                    p2 += 1

        # Process any remaining elements in nums1.
        while p1 < n:
            if not res or res[-1] != nums1[p1]:
                res.append(nums1[p1])
            curr = nums1[p1]
            while p1 < n and nums1[p1] == curr:
                p1 += 1

        # Process any remaining elements in nums2.
        while p2 < m:
            if not res or res[-1] != nums2[p2]:
                res.append(nums2[p2])
            curr = nums2[p2]
            while p2 < m and nums2[p2] == curr:
                p2 += 1

        return res
