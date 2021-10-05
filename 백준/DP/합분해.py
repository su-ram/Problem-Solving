N,K = map(int, input().split())
dp = [ [1]*(K+1) for _ in range(N+1)]

if K > 1:
    for i in range(2, K+1):
        for j in range(1, N+1):
            dp[j][i] = dp[j-1][i] + dp[j][i-1]

print(dp[-1][-1] % 1000000000)