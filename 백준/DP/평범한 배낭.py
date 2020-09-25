N, limit = map(int,input().split())
weight = [0]
value = [0]
for _ in range(N):
    a,b = map(int, input().split())
    weight.append(a)
    value.append(b)

dp = []

for i in range(N+1):
    temp = [0]*(limit+1)
    dp.append(temp)


for i in range(1,N+1):
    for j in range(1,limit+1):
        if weight[i] <= j :
            dp[i][j] = max(value[i]+dp[i-1][j-weight[i]],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        pass


print(dp[-1][-1])