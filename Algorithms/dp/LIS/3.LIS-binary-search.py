
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        for i in range(len(nums)):
            if nums [i] > dp[-1]:
                dp.append(nums[i])

            else:
                idx = bisect.bisect_left(dp, nums[i])
                dp[idx] = nums[i]

        return len(dp)

s=Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
