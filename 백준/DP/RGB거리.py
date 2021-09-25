N = int(input())
rgb = [ list(map(int, input().split())) for _ in range(N)]
dp = [ [0]*(N+1) for _ in range(3)]

dp[0][1] = rgb[0][0]
dp[1][1] = rgb[0][1]
dp[2][1] = rgb[0][2]

for i in range(2, N+1):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + rgb[i-1][0]
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + rgb[i-1][1]
    dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + rgb[i-1][2]

print(min(dp[0][-1], dp[1][-1], dp[2][-1]))