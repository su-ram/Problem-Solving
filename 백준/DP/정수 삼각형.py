N = int(input())
nums = [ list(map(int, input().split())) for _ in range(N)]

dp = [ [0]*(N+1) for _ in range(N+1)]
dp[1][1] = nums[0][0]
for i in range(2, N+1):
    for j in range(1, i+1):
        if j == 1 :
            dp[i][j] = dp[i-1][j] + nums[i-1][j-1]
        if j == i :
            dp[i][j] = dp[i-1][j-1] + nums[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i-1][j-1]

print(max(dp[-1]))
