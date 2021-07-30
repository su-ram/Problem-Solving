grid = [ [1, 2], [3, 4] ]

from collections import deque
import math
row, col = (len(grid), len(grid[0]))
path = [[math.inf]*col for _ in range(row)]
que = deque([(0,0,0)])
dx = [0,1]
dy = [1,0]

while que:
    node = que.popleft()
    x , y = node[:2]
    path[x][y] = min(path[x][y], grid[x][y] + node[-1])

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row and 0 <= ny < col :
            que.append((nx,ny,path[x][y]))

print(path[row-1][col-1])
