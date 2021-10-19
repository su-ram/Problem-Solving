field = [ list(input()) for _ in range(12)]
from collections import deque



def pop(field):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    changed = 0

    visited = [ [False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and visited[i][j] is False:
                color = field[i][j]
                group = set([(i,j)])
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == color and (nx,ny) not in group:
                            q.append((nx,ny))
                            group.add((nx,ny))

                if len(group) >= 4:
                    changed = 1
                    for x, y in group:
                        field[x][y] = '.'
                        visited[x][y] = True





    return changed






def drop(field):

    for j in range(6):
        index = -1
        arr = []
        for i in range(11, -1, -1):
            if index == -1 and field[i][j] ==  '.':
                index = i
            elif index != -1 and field[i][j] != '.':
                arr.append(field[i][j])
        for i in range(len(arr)):
            field[index- i][j] = arr[i]

        for x in range(index - len(arr), -1, -1):
            field[x][j] = '.'



def solution(field):

    cnt = 0
    while True:
        changed = pop(field)
        drop(field)
        if changed == 0:
            break
        cnt += changed
    return cnt


print(solution(field))