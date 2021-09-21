N = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
maps = [[0]*101 for _ in range(101)]
result = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    maps[x][y] = 1
    moves = [d]

    for _ in range(g):
        temp = []
        for i in range(len(moves)):
            temp.append((moves[-i - 1] + 1) % 4)
        moves.extend(temp)

    for move in moves:
        nx = x + dx[move]
        ny = y + dy[move]
        maps[nx][ny] = 1
        x = nx
        y = ny

for i in range(100):
    for j in range(100):
        if maps[i][j] == 1 :
            if maps[i+1][j] == 1 and maps[i+1][j+1] == 1 and maps[i][j+1] == 1 :
                result += 1

print(result)

