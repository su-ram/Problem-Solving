N, L, R = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(N)]

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(start, visited):
    q = deque([start])
    total = A[start[0]][start[1]]
    units = [start]
    visitnode = [[False] * N for _ in range(N)]
    while q :
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                diff = abs(A[nx][ny] - A[x][y])
                if L <= diff <= R and visited[nx][ny] is False and visitnode[nx][ny] is False:
                    q.append((nx,ny))
                    total += A[nx][ny]
                    units.append((nx,ny))
                    visitnode[nx][ny] = True
    return units, total // len(units)


result = 0
while True :
    visited = [[False] * N for _ in range(N)]
    union = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] is False:
                visited[i][j] = True
                units, num = BFS((i, j), visited)
                cnt += 1
                for u in units:
                    union.append((u, num))
                    visited[u[0]][u[1]] = True

    for u in union:
        pos = u[0]
        n = u[1]
        A[pos[0]][pos[1]] = n
    if cnt == N**2:
        break
    result += 1
print(result)