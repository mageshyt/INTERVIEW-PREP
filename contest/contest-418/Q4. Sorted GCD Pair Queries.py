
from collections import Counter
from itertools import combinations
from math import gcd
from collections import Counter

class Solution:
    def gcdValues(self, nums, queries):
        n = len(nums)
        gcd_counter = Counter()

        for i in range(n):
            for j in range(i + 1, n):
                gcd_value = gcd(nums[i], nums[j])
                gcd_counter[gcd_value] += 1

        max_gcd = max(gcd_counter.keys(), default=0)

        cumulative_count = [0] * (max_gcd + 1)
        for i in range(1, max_gcd + 1):
            cumulative_count[i] = cumulative_count[i - 1] + gcd_counter[i]

        total_pairs = n * (n - 1) // 2
        answer = []

        for query in queries:
            if 0 <= query < total_pairs:
                left, right = 1, max_gcd
                while left < right:
                    mid = (left + right) // 2
                    if cumulative_count[mid] <= query:
                        left = mid + 1
                    else:
                        right = mid
                answer.append(left)
            else:
                answer.append(None)  # For invalid queries, return None

        return answer

# Example usage
nums = [2, 3, 4]
queries = [0, 2, 2]
solution = Solution()
result = solution.gcdValues(nums, queries)
print(result)  # Expected output: [1, 2, 2]
