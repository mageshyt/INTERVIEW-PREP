from collections import Counter

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        MOD = 10**9 + 7
        total = sum(int(d) for d in num)

        if n % 2 or total % 2:
            return 0
        
        target = total // 2
        freq = Counter(num)
        memo = {}

        def getState(pos, left_sum, right_sum):
            counts = tuple(freq[d] for d in sorted(freq))
            return (pos, left_sum, right_sum, counts)

        def backtrack(pos, left_sum, right_sum):
            if left_sum > target or right_sum > target:
                return 0
            
            if pos == n:
                return 1 if left_sum == right_sum else 0
            
            state = getState(pos, left_sum, right_sum)
            if state in memo:
                return memo[state]

            curr = 0
            for d in freq:
                if freq[d] == 0:
                    continue
                
                freq[d] -= 1
                if pos % 2 == 0:
                    curr = (curr + backtrack(pos + 1, left_sum + int(d), right_sum)) % MOD
                else:
                    curr = (curr + backtrack(pos + 1, left_sum, right_sum + int(d))) % MOD
                freq[d] += 1

            memo[state] = curr
            return curr

        return backtrack(0, 0, 0)

# Example usage:
solution = Solution()
result = solution.countBalancedPermutations("123")
print(result)  # Example to test   test_balanced_permutations()
