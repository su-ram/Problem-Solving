
n = int(input())
meetings = []

for i in range(n):

    tmp = list(map(int, input().split()))
    meetings.append(tmp)

dp = [0] * (n+1)
not_finished = []

for i in range(1, n+1):
    tmp = tuple(meetings[i-1] + [dp[i-1], i + meetings[i-1][0] - 1])
    not_finished.append(tmp)

    for j in not_finished:

        if j[-1] == i :
            dp[i] = max(dp[i-1], sum(j[1:3]), dp[i])

    if dp[i] == 0 :
        dp[i] = dp[i-1]

print(dp[-1])
