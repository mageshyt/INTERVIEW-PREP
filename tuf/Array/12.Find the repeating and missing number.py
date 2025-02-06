from collections import defaultdict


class Solution:
    def findMissingRepeatingNumbers(self, nums):
        numMap=defaultdict(int)

        repeat=-1

        for num in nums:
             if num not in numMap:
                 numMap[num]+=1
             else:
                 repeat=num


        for i in range(1,len(nums)+1):
             if i not in numMap:
                 return [repeat,i]

    
        return [-1,-1]
