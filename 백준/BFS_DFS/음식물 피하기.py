
from collections import deque

R, C, K = map(int, input().split())
matrix = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    x, y = map(int, input().split())
    matrix[x][y] = 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def BFS(start, visited):
    q = deque([start])
    cnt = 0
    while q:
        x,y = q.popleft()

        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= R and 1 <= ny <= C:
                if (nx, ny) not in visited and matrix[nx][ny] == 1:
                    q.append((nx,ny))
                    visited.append((nx, ny))
    return cnt


visited = []
result = -1
for i in range(1, R+1):
    for j in range(1, C+1):
        if (i,j) not in visited and matrix[i][j] == 1:
            visited.append((i, j))
            result = max(BFS((i,j), visited), result)

print(result)