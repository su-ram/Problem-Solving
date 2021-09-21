N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int,input().split()))
dp = [ [0]*(sum(cost)+1) for _ in range(N+1)]
result = sum(cost) + 1
for i in range(1, N+1):
    for j in range(1, sum(cost)+1):
        if j < cost[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
        if dp[i][j] >= M:
            result = min(result, j)
print(result)
