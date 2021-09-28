N, M = map(int, input().split())
result = 1

dir = [(-2,1), (-1,2), (1,2),(2,1)]
visited = set()
from collections import deque
import copy

def BFS(start):
    q = deque([start])
    visited.add((start[0], start[1]))
    global result
    while q:
        x,y,d,c = q.popleft()
        check = c
        if d > 4 and 0 in check : continue

        result = max(result, d)
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                newcheck = copy.deepcopy(check)
                newcheck[i] = 1
                q.append((nx,ny,d+1,newcheck))
                visited.add((nx,ny))

BFS((N-1,0,1,[0]*4))
print(result)



