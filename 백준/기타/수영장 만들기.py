n,m = map(int,input().split())
from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = 0
pool = [list(map(int, list(input()))) for _ in range(n)]

def BFS(start, height):
    que = deque([start])
    global visited,result
    visited[start[0]][start[1]] = True
    over = False
    cnt = 1

    while que :
        now = que.popleft()
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]

            if xx >= n or xx < 0 or yy >= m or yy < 0 :
                over = True
                continue

            if visited[xx][yy] == False and pool[xx][yy] <= height:
                que.append((xx,yy))
                visited[xx][yy] = True
                cnt += 1
    if not over:
        result += cnt

for height in range(1,9):
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):

            if pool[i][j] <= height and not visited[i][j] :
                BFS((i,j), height)
print(result)

