n = int(input())
lines = [ tuple(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x :x[0])

dp = [0] * n
dp[0] = 1


for i in range(1, n):
    for j in range(i):
        if lines[j][1] < lines[i][1] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
    #dp[i] = max(dp[i-1], dp[i])

print(n - max(dp))