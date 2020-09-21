import sys

# DFS 백트래킹을 이용하는 문제. 공부 더 필요......ㅠ
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def promising(x, y):
    if 0 <= x < r and 0 <= y < c and pool[ord(matrix[x][y]) - 65] == 0:
        return True
    else:
        return False
def DFS(start, cnt):
    global maxcnt
    if cnt == 26:
        maxcnt = 26
        return
    else:
        maxcnt = max(cnt, maxcnt)

    x = start[0]
    y = start[1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if promising(xx, yy):
            pool[ord(matrix[xx][yy]) - 65] = 1
            DFS((xx, yy), cnt+1)
            pool[ord(matrix[xx][yy]) - 65] = 0

r, c = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(r)]
pool = [0] * 26
pool[ord(matrix[0][0]) - 65] = 1
maxcnt = 0
DFS((0, 0),1)
print(maxcnt)