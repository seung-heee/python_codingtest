def tile_fill(N):
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

N = 10
result = tile_fill(N)
print(result)  # Output: 89