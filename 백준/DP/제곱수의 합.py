n = int(input())
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = i

if n > 1:
    for i in range(2, int(n**0.5)+1):
        for j in range(i*i, n+1):
            dp[j] = min(dp[j], dp[j-i*i]+1)


print(dp[-1])