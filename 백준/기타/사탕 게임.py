n = int(input())
b = [list(input()) for _ in range(n)]
from collections import deque


def counting(b, start, dirs):
    num = 0
    visited = [ [False]*len(b) for _ in range(len(b))]

    for dir in dirs:
        color = b[start[0]][start[1]]
        q = deque([start])
        check = set()
        while q:
            x, y = q.popleft()
            for d in dir:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < len(b) and 0 <= ny < len(b) and b[nx][ny] == color and (nx, ny) not in check:
                    q.append((nx, ny))
                    check.add((nx, ny))
        num = max(num, len(check))
        for x, y in check:
            visited[x][y] = True

    return num


def swap(b):

    visited = set()
    # 0010
    dirs = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
    num = 0

    for dir in dirs:
        visited = [[False] * len(b) for _ in range(len(b))]
        for i in range(len(b)):
            for j in range(len(b)):
                if visited[i][j] is False:
                    color = b[i][j]
                    q = deque([(i, j)])
                    check = set()
                    while q:
                        x, y = q.popleft()
                        for d in dir:
                            nx = x + d[0]
                            ny = y + d[1]
                            if 0 <= nx < len(b) and 0 <= ny < len(b) and b[nx][ny] == color and (nx, ny) not in check:
                                q.append((nx, ny))
                                check.add((nx, ny))
                    num = max(num, len(check))
                    for x, y in check:
                        visited[x][y] = True


    visited = set()
    for i in range(len(b)):
        for j in range(len(b)):
            color = b[i][j]
            for d in dirs[0] + dirs[1]:
                nx = i + d[0]
                ny = j + d[1]
                if 0 <= nx < len(b) and 0 <= ny < len(b) and b[nx][ny] != color:
                    index1 = str(i) + str(j) + str(nx) + str(ny)
                    index2 = str(nx) + str(ny) + str(i) + str(j)
                    if index1 not in visited and index2 not in visited:
                        b[i][j], b[nx][ny] = b[nx][ny], b[i][j]
                        cnt = counting(b, (i,j), dirs)
                        num = max(num, cnt)
                        cnt = counting(b, (nx,ny), dirs)
                        num = max(num, cnt)
                        b[i][j], b[nx][ny] = b[nx][ny], b[i][j]
                        visited.add(index1)


    return num

print(swap(b))

# 초기 상태에서 연속된 같은 사탕 개수 카운팅
# 인접한 다른 것들 교환후 체크 
# 카운팅하는 메소드, 교환하는 메소드 구현 