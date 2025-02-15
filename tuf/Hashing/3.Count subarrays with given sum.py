class Solution:
    def subarraySum(self, nums, k):
        n=len(nums)
        prefixMap= { 0:1 } 
        current_sum=0
        count=0


        for i in range(n):
            current_sum+=nums[i]
            target=current_sum-k
            if target in prefixMap:
                count+=prefixMap[target]
            prefixMap[current_sum]=prefixMap.get(current_sum,0)+1

        return count


s=Solution()

print(s.subarraySum([1,2,3,4,5],3))
