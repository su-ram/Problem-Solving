r, c = map(int, input().split())
matrix = [ list(input()) for _ in range(r)]
from collections import deque
import copy

def BFS(start, treasure):
    que = deque([start])
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = [[False] * c for _ in range(r)]

    while que:
        now = que.popleft()
        visited[now[0]][now[1]] = True

        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]

            if 0 <= xx < r and 0 <= yy < c and treasure[xx][yy] == 'L' and visited[xx][yy] == False:
                treasure[xx][yy] = now[2] + 1
                que.append((xx,yy,now[2]+1))
                global dist
                if treasure[xx][yy] > dist:
                    dist = treasure[xx][yy]


dist = -1
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'L':
            BFS((i,j,0), copy.deepcopy(matrix))

print(dist)