
T = int(input())


for t in range(T):
    n, k, p = map(int, input().split())
    plates = []
    for _ in range(n):
        plates.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(1,k):
            plates[i][j] += plates[i][j-1]
        plates[i].append(0)


    dp = [[0]*(p+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(p+1):
            for x in range(min(j,k)+1):
                dp[i][j] = max(dp[i][j], plates[i-1][x-1] + dp[i - 1][j - x])


    print("Case #%d: %d" %(t+1, dp[-1][-1]))