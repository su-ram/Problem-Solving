N, M = map(int,input().split())
field = [ list(input()) for _ in range(M)]
from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [ [False] * N for _ in range(M)]

def BFS(start, team):
    cnt = 1
    que =deque([start])
    visited[start[0]][start[1]] = True

    while que :
        now = que.popleft()
        for i in range(4):
            nx, ny = now[0] +dx[i], now[1] +dy[i]

            if 0<=nx < M and 0 <= ny < N and field[nx][ny] == team and visited[nx][ny] is False:
                que.append((nx,  ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt ** 2


result = {'W':0, 'B':0}

for i in range(M):
    for j in range(N):
        if field[i][j] in ['W', 'B'] and visited[i][j] is False:
            result[field[i][j]] = result.get(field[i][j]) + BFS((i,j), field[i][j])

print(result.get('W'), result.get('B'))

