class Solution:
    def longestSubarray(self, nums, k):
        if not nums:
            return 0

        prefixMap = {}
        max_len=0
        current_sum = 0

        for idx,num in enumerate(nums):
            current_sum+=num

            if current_sum == k:
                max_len = max(max_len,idx+1)

            target = current_sum - k

            if target in prefixMap:
                newLength=idx-prefixMap[target]
                max_len = max(max_len,newLength)

            if current_sum not in prefixMap:

                prefixMap[current_sum] = idx

        return max_len

    # sliding window (only for positive numbers)
    def longestSubarray(self, nums, k):
        if not nums:
            return 0

        left, right = 0, 0

        current_sum = 0

        max_len = 0

        while right < len(nums):
            current_sum += nums[right]

            if current_sum == k:
                max_len = max(max_len, right - left + 1)
            
            while current_sum > k:
                current_sum -= nums[left]
                left += 1

            right+=1



        return max_len




s=Solution()

print(s.longestSubarray([1,2,3,4,5],3))
