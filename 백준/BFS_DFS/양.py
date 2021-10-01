R, C = map(int, input().split())
field = [ list(input()) for _ in range(R)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

from collections import deque

def BFS(start, totalvisited):
    q = deque([start])
    visited = set()
    visited.add(start)
    totalvisited.add(start)
    sheep = 0
    wolf = 0

    while q:
        x,y=q.popleft()
        if field[x][y] == 'o': sheep += 1
        if field[x][y] == 'v': wolf += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if field[nx][ny] != '#' and (nx,ny) not in visited:
                    q.append((nx,ny))
                    totalvisited.add((nx,ny))
                    visited.add((nx,ny))


    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0

    return sheep, wolf


totalvisited = set()
sheep, wolf = 0,0

for i in range(R):
    for j in range(C):
        if field[i][j] != '#' and (i,j) not in totalvisited:
            s, w = BFS((i,j), totalvisited)
            sheep += s
            wolf += w


print(sheep, wolf)