n, m = map(int,input().split())
a = [ list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
from collections import deque


def BFS(start, total_visit):
    q = deque([start])
    isvisit = set()
    isvisit.add(start)
    total = 0

    while q:
        x,y = q.popleft()
        total += 1
        total_visit.add((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1 and (nx,ny) not in isvisit:
                q.append((nx,ny))
                isvisit.add((nx,ny))
    return total


total_visit = set()
total = 0
area = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and (i,j) not in total_visit:
            area = max(area, BFS((i,j), total_visit))
            total += 1

print(total, area)