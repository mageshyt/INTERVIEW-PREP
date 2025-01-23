
class Solution:
    def minCost(self, cost, n):
        # Create a DP table to store the minimum cost for each house and color combination
        dp = [[float('inf')] * 3 for _ in range(n)]

        # Initialize the first house with the given costs
        for color in range(3):
            dp[0][color] = cost[0][color]

        # Fill the DP table
        for house in range(1, n):
            for color in range(3):
                # Find the minimum cost from the previous house, excluding the current color
                min_prev_cost = float('inf')
                for prev_color in range(3):
                    if prev_color != color:
                        min_prev_cost = min(min_prev_cost, dp[house - 1][prev_color])

                # Assign the minimum cost to the current house and color
                dp[house][color] = cost[house][color] + min_prev_cost

        # Now, handle the equidistant pairs
        for i in range(n // 2):
            j = n - i - 1
            for color_i in range(3):
                for color_j in range(3):
                    if color_i != color_j:
                        # Update the cost for the pair (i, j)
                        dp[i][color_i] = min(dp[i][color_i], cost[i][color_i] + dp[j][color_j])
                        dp[j][color_j] = min(dp[j][color_j], cost[j][color_j] + dp[i][color_i])

        # The minimum cost will be the minimum value in the last row of the DP table
        return min(dp[-1])

# Example usage:
solution = Solution()
n = 6
cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]
print(solution.minCost(cost, n))  # Output should be 18

