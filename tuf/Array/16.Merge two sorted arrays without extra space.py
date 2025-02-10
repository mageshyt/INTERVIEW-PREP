class Solution:
    def merge(self, nums1, m, nums2, n):
        res=[]
        p1,p2=0,0

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1

        while p1 < m:
            res.append(nums1[p1])
            p1+=1

        while p2 < n:
            res.append(nums2[p2])
            p2+=1

        for i in range(m+n):
            nums1[i]=res[i]

        return nums1


