from collections import deque

N, M = map(int, input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
a = [ list(map(int, input().split())) for _ in range(N)]


def aired():
    q = deque([(0,0)])
    visited = [ [False]*M for _ in range(N)]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if a[nx][ny] >= 1:
                    a[nx][ny] += 1
                elif a[nx][ny] == 0 and visited[nx][ny] is False:
                    q.append((nx,ny))
                    visited[nx][ny] = True


def melt_cheese():
    for i in range(N):
        for j in range(M):
            if a[i][j]>=3:
                a[i][j] = 0
            elif a[i][j] > 0:
                a[i][j] = 1


def all_melted():
    for i in range(N):
        for j in range(M):
            if a[i][j] != 0:
                return False
    return True


days = 0
while True:
    aired()
    melt_cheese()
    days += 1
    if all_melted():
        break

print(days)