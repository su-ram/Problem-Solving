n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [ list(map(int, input().split())) for _ in range(n)]

stopped = False
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cleaned = 0

def next():
    nd = d - 1
    if nd < 0 : nd = 3
    return x + dx[nd], y + dy[nd]


def turnleft():
    global d, cnt
    d -= 1
    if d < 0 : d = 3


def moveback():
    global d
    return x - dx[d], y - dy[d]


while not stopped :

    if maps[x][y] == 0 :
        maps[x][y] = -1
        cleaned += 1

    cnt = 0
    for i in range(4):
        nx, ny = next()
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0 :
            turnleft()
            x , y = nx, ny
            break
        turnleft()
        cnt += 1

    if cnt == 4 :
        bx, by = moveback()
        if 0 <= bx < n and 0 <= by < m and maps[bx][by] <= 0 :
            x, y = bx, by
        else:
            stopped = True


print(cleaned)