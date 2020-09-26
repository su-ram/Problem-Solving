T = int(input())

for _ in range(T):
    num = int(input())
    dp = [[0]*(num+1) for _ in range(4)]

    for i in range(4):
        for j in range(num+1):
            if i == 1:
                dp[i][j] = 1
            if j == 0 :
                dp[i][j] = 0
            elif i > j :
                dp[i][j] = dp[i-1][j]
            elif j == i :
                dp[i][j] = dp[i-1][j]+1
            else:
                dp[i][j] = sum(dp[i][j-i:j])
                
    print(dp[-1][-1])