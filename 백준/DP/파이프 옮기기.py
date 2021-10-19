n = int(input())
wall = [[0]*(n+1)]
for _ in range(n):
    wall.append([0]+ list(map(int, input().split())))

def solution(n, wall):

    dp = [ [ [0]*3 for _ in range(n+1) ] for _ in range(n+1)]
    dp[1][2] = [1,0,0]

    for i in range(1, n+1):
        for j in range(3, n+1):
            if wall[i][j] == 1:continue
            if wall[i][j-1] != 1:
                dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
            if wall[i-1][j] != 1:
                dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
            if wall[i-1][j-1] != 1:
                if wall[i-1][j] != 1 and wall[i][j-1] != 1:
                    dp[i][j][2] += sum(dp[i-1][j-1])

    return sum(dp[-1][-1])


print(solution(n, wall))