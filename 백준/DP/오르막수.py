N = int(input())
dp = [ [1]*(N+1) for _ in range(10)]
for i in range(1, N+1):
    for j in range(1,10):
        dp[j][i] = dp[j-1][i] + dp[j][i-1]

print(dp[-1][-1] % 10007)