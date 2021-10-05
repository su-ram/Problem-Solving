n, k = map(int, input().split())
v = [ int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1

for i in range(n):
    value = v[i]
    for j in range(value, k+1):
        dp[j] = dp[j] + dp[j-value]

print(dp[-1])