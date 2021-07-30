N, M = map(int, input().split())
coins = [ int(input()) for _ in range(N)]

import math
dp = [math.inf]*(M+1)
dp[0] = 0

for i in coins:
    for j in range(i, M+1):
        dp[j] = min(dp[j], dp[j-i] + 1) if dp[j-i] != math.inf else dp[j]

print(dp)
