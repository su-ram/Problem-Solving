R, C = map(int,input().split())
swans = []
maps = []
for i in range(R):
    row = list(input())
    maps.append(row)
    for j in range(C):
        if row[j] == 'L':
            swans.append((i,j))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
time = [[0]*C for _ in range(R)]
from collections import deque

def melt_time():
    visited = [ [False]*C for _ in range(R)]
    que = deque()
    for i in range(R):
        for j in range(C):
            if maps[i][j] == '.' or maps[i][j] == 'L':
                que.append((i,j))
                time[i][j] = 0
                visited[i][j] = True
    last = 0
    while que:
        i,j = que.popleft()
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maps[nx][ny] != 'L':
                que.append((nx,ny))
                visited[nx][ny] = True
                time[nx][ny] = time[i][j] + 1
                last = time[nx][ny]
    return last


def connect(start, days):
    visited = [[False] * C for _ in range(R)]
    que = deque([start])
    visited[start[0]][start[1]] = True
    while que :
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] is False:
                visited[nx][ny] = True
                if (nx, ny) == swans[1]:
                    return True
                if time[nx][ny] <= days:
                    que.append((nx,ny))

    return False


left, right = 0, melt_time()
result = right
while left <= right:
    mid = (left+right) // 2
    if connect(swans[0], mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1
print(result)


