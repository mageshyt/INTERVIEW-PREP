"""
Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays.



The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.


Examples:
Input: arr1 = [2, 4, 6], arr2 = [1, 3, 5]

Output: 3.5

Explanation: The array after merging arr1 and arr2 will be [ 1, 2, 3, 4, 5, 6 ]. As the length of the merged list is even, the median is the average of the two middle elements. Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.

Input: arr1 = [2, 4, 6], arr2 = [1, 3]

Output: 3.0

Explanation: The array after merging arr1 and arr2 will be [ 1, 2, 3, 4, 6 ]. The median is simply 3.

Input: arr1 = [2, 4, 5], arr2 = [1, 6]

Output:
4.0
"""

class Solution:
    def median(self, arr1, arr2):
        n1,n2=len(arr1),len(arr2)

        total=n1+n2

        idx2=total//2
        idx1=idx2-1
        cnt=0

        i,j=0,0

        idx1_val,idx2_val=-1,-1

        while i<n1 and j<n2:
            if arr1[i] < arr2[j]:
                if cnt == idx1:
                    idx1_val=arr1[i]

                if cnt == idx2:
                    idx2_val=arr1[i]

                i+=1

            else:
                if cnt == idx1:
                    idx1_val=arr2[j]

                if cnt == idx2:
                    idx2_val=arr2[j]

                j+=1

            cnt+=1

        while i<n1:
            if cnt == idx1:
                idx1_val=arr1[i]

            if cnt == idx2:
                idx2_val=arr1[i]

            i+=1
            cnt+=1

        while j<n2:
            if cnt == idx1:
                idx1_val=arr2[j]

            if cnt == idx2:
                idx2_val=arr2[j]

            j+=1
            cnt+=1

        if total%2==0:
            return (idx1_val+idx2_val)/2

        return idx2_val


