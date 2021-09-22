N = int(input())
dp = [0] * (N+1)
dp[1] = 1 % 10007
if N > 1 :
    dp[2] = 3 % 10007
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]*2) % 10007
print(dp[N])