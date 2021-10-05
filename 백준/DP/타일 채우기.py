n = int(input())
dp = [0] *(31)
dp[2] = 3

for i in range(4, 31):
    dp[i] = dp[i-2] * 3 + dp[i-4]*2
    if i% 2 == 0:
        num = 4
        while num + 2 <= i:
            num += 2
            dp[i] += (dp[i-num] * 2)
        dp[i] += 2


print(dp[n])
