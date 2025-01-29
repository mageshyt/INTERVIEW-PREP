from collections import deque

class Solution:
    def leaders(self, nums):
        q=deque([nums[-1]])
        leader=nums[-1]

        for i in range(len(nums)-2,-1,-1):

            if leader < nums[i]:
                q.appendleft(nums[i])
                leader=nums[i]

        return list(q)


s=Solution()

print(s.leaders([1,2,5,3,1,2]))
