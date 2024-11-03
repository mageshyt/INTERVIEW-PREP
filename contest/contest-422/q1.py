class Solution:
    def isBalanced(self, num: str) -> bool:
        nums = list(map(int,num))

        n = len(nums)

        even = 0
        odd = 0

        for i in range(n):
            if i%2 == 0:
                even += nums[i]
            else:
                odd += nums[i]

        return even == odd

print(Solution().isBalanced("1234")) # True
print(Solution().isBalanced("24123")) # False
