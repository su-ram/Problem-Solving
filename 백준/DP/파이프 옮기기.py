n = int(input())
wall = []
for _ in range(n):
    wall.append(list(map(int, input().split())))

from collections import deque


# def solution(n, wall):
#
#     dp = [ [ [0]*3 for _ in range(n+1) ] for _ in range(n+1)]
#     dp[1][2] = [1,0,0]
#
#     for i in range(1, n+1):
#         for j in range(3, n+1):
#             if wall[i][j] == 1:continue
#             if wall[i][j-1] != 1:
#                 dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
#             if wall[i-1][j] != 1:
#                 dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
#             if wall[i-1][j-1] != 1:
#                 if wall[i-1][j] != 1 and wall[i][j-1] != 1:
#                     dp[i][j][2] += sum(dp[i-1][j-1])
#
#     return sum(dp[-1][-1])
#
#
# print(solution(n, wall))


def dfs(x,y,form, wall):
    if x == length -1 and y == length -1 :
        global visited
        visited +=1
        return

    for dx, dy, f in moves[form]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < length and 0 <= ny < length and wall[nx][ny] != 1:
            if f == 2 and (wall[nx-1][ny]== 1 or wall[nx][ny-1] == 1):continue
            dfs(nx,ny,f, wall)


def solution(n, wall):
    global visited, moves, length
    length = n
    visited = 0
    moves = [
        [[0, 1, 0], [1, 1, 2]],
        [[1, 0, 1], [1, 1, 2]],
        [[0, 1, 0], [1, 0, 1], [1, 1, 2]]
    ]
    dfs(0,1,0,wall)

    return visited


print(solution(n, wall))