n = int(input())
dp = [0]*(n)
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] :
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))