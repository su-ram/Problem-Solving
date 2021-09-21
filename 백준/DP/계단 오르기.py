N = int(input())
points = [int(input()) for _ in range(N)]
dp = [0] * (N+1)
dp[1] = points[0]
if N > 1 :
    dp[2] = points[0] + points[1]
    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + points[i-2]+ points[i-1], dp[i-2] +points[i-1])
print(dp[-1])

