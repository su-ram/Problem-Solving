
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[1] * (M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if i > j :
                dp[i][j] = 0
            elif i == j :
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[-1][-1])
