from collections import defaultdict
class Solution:
    def subarraysWithXorK(self, nums, k):
        prefixMap = defaultdict(int)
        prefixMap[0] = 1
        current_xor = 0
        count = 0

        for num in nums:
            current_xor ^= num
            target = current_xor ^ k
            count += prefixMap[target]
            prefixMap[current_xor] += 1

        return count


