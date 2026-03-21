def minCoins(coins, N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, N + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[N] if dp[N] != float('inf') else -1