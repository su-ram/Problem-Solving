n = int(input())
dp = [(n, n)] * (n+1)
dp[-1] = (0,0)
for i in range(n,-1,-1):
    if i %3 == 0:
        if dp[i][0] + 1 < dp[i//3][0] :
            dp[i//3] = (dp[i][0]+1, i)

    if i % 2 == 0:
        if dp[i][0] + 1 < dp[i//2][0] :
            dp[i//2] = (dp[i][0]+1, i)

    if i > 1:
        if dp[i][0] + 1 < dp[i-1][0]:
            dp[i-1] = (dp[i][0]+1, i)

arr = []
now = 1
while True:
    arr.append(now)
    if now == n:
        break
    now = dp[now][1]
print(len(arr)-1)
print(' '.join(map(str, arr[::-1])))
