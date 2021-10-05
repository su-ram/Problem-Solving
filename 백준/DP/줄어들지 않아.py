
dp = [ [1]*(65) for _ in range(10)]

for i in range(1, 10):
    for j in range(2, 65):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for i in range(int(input())):
    N = int(input())
    result = 0
    for j in range(10):
        result +=dp[j][N]
    print(result)