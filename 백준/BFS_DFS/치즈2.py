R, C = map(int, input().split())
cheese = [ list(map(int, input().split())) for _ in range(R)]

from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def aired():
    start = (0,0)
    q = deque([start])
    aired = set()
    visited = set()

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if cheese[nx][ny] == 0 and (nx,ny) not in visited:
                    q.append((nx,ny))
                    visited.add((nx,ny))
                if cheese[nx][ny] == 1:
                    aired.add((nx,ny))

    for pos in aired:
        cheese[pos[0]][pos[1]] = 0

    return aired


def check():
    for i in range(R):
        for j in range(C):
            if cheese[i][j] == 1:
                return False
    return True


melted_cheese = 0
days = 0
while True:
    melted_cheese = len(aired())
    days  += 1
    if check():
        break

print(days)
print(melted_cheese)
