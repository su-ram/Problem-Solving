N = int(input())
arr = list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[1][i] = dp[1][i-1] + arr[0]

if N > 1:
    for i in range(2, N+1):
        for j in range(1, N+1):
            if j < i :
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-i]+arr[i-1])

print(dp[-1][-1])