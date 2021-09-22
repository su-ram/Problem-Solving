N = int(input())
dp = [N+1] * (N+1)
n = int(N**0.5)
for i in range(n):
    square = (i+1) ** 2
    dp[square] = 1
    for j in range(square + 1, N+1):
        dp[j] = min(dp[j-square] + 1, dp[j])
print(dp[-1])

