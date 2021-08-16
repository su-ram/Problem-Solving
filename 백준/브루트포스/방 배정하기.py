a, b, c, n = map(int, input().split())
dp = [0] * (n+1)
dp[0] = 1
for r in [a, b, c]:
    for i in range(r, n+1, 1):
        dp[i] += dp[i-r]
print(1 if dp[-1] else 0)