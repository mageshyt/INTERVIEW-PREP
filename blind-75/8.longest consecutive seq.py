class Solution:
    def longestConsecutive(self, nums) -> int:
        uniqueNums = set(nums)
        maxLen = 0
        for num in uniqueNums:
            # check if num is the start of a sequence
            if num -1 not in uniqueNums:
                currentNum = num
                currentLen = 1
                while currentNum + 1 in uniqueNums:
                    currentNum += 1
                    currentLen += 1

                maxLen = max(maxLen, currentLen)



        return maxLen

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
