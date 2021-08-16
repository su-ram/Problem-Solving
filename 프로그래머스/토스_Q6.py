def solution(numOfStairs):
    dp = [0] * (numOfStairs+1)
    dp[0] = 1
    dp[1] = 1
    if numOfStairs > 1 :
        dp[2] = 2
        for i in range(3, numOfStairs+1):
            dp[i] = sum(dp[i-3 : i])
    return dp[-1]

print(solution(3))