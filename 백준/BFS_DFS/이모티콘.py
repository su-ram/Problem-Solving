s = int(input())

def solution(s):

    dp = [ [s*s] * (s+1) for _ in range(s+1)]
    dp[1][0] = 0

    for i in range(1, s+1):
        for j in range(s+1):
            dp[i][i] = min(dp[i][i], dp[i][j]+1)
            if i + j <= s:
                dp[i+j][j] = min(dp[i+j][j], dp[i][j] + 1)
            if i - 1 >= 0:
                dp[i-1][j] = min(dp[i-1][j], dp[i][j] + 1)

    print(min(dp[-1][1:]))

solution(s)