MOD = 1000000007

def calculate_row_ways(m):
    ways = [0] * (m + 1)
    ways[0] = 1
    for i in range(1, m + 1):
        if i >= 1:
            ways[i] = (ways[i] + ways[i - 1]) % MOD
        if i >= 2:
            ways[i] = (ways[i] + ways[i - 2]) % MOD
        if i >= 3:
            ways[i] = (ways[i] + ways[i - 3]) % MOD
        if i >= 4:
            ways[i] = (ways[i] + ways[i - 4]) % MOD
    return ways[m]

def count_lego_wall_ways(n, m):
    row_ways = calculate_row_ways(m)
    full_wall_ways = pow(row_ways, n, MOD)
    
    dp = [0] * (m + 1)
    dp[0] = 1
    
    for width in range(1, m + 1):
        total_ways = pow(calculate_row_ways(width), n, MOD)
        for j in range(1, width):
            total_ways = (total_ways - dp[j] * pow(calculate_row_ways(width - j), n, MOD)) % MOD
        dp[width] = total_ways
    
    return dp[m]

def calculate_lego_wall(height, width):
    return count_lego_wall_ways(height, width)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    result = calculate_lego_wall(n, m)
    print(result)
