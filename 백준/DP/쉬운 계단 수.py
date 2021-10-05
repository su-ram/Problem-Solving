N = int(input())
dp = [[1]*(N+1) for _ in range(10)]
dp[0][1] = 0

for i in range(2, N+1):
    for j in range(10):
        if j == 0 :
            dp[j][i] = dp[j+1][i-1]
        elif 1 <= j < 9:
            dp[j][i] = dp[j-1][i-1] + dp[j+1][i-1]
        else:
            dp[j][i] = dp[j-1][i-1]

result = 0
for i in range(10):
    result += dp[i][N]
print(result%1000000000)