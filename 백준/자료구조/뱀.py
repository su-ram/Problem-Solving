N = int(input())
A = int(input())
apples = []
for _ in range(A):
    pos = list(map(int, input().split()))
    pos = list(map(lambda x : x-1, pos))
    apples.append(pos)

L = int(input())
shifts = []
for shift in range(L):
    sec, dir = input().split()
    sec = int(sec)
    shifts.append((sec, dir))

board = [[0]*N for _ in range(N)]
for a in apples:
    board[a[0]][a[1]] = 1
D = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
head = (0,0)
cnt = 0

from collections import deque
shifts = deque(shifts)
snake = deque([head])

while True :

    if shifts:
        if cnt == shifts[0][0]:
            sec, dir = shifts.popleft()
            if dir == 'L':
                D -= 1
                if D == -1 :
                    D = 3
            if dir == 'D':
                D += 1
                if D == 4 :
                    D = 0

    nx = head[0] + dx[D]
    ny = head[1] + dy[D]
    cnt += 1

    if nx < 0 or nx >= N or ny < 0 or ny >= N :
        break
    if snake.count((nx, ny)) :
        break

    snake.appendleft((nx, ny))

    if board[nx][ny] == 0 :
        snake.pop()
    if board[nx][ny] == 1 :
        board[nx][ny] = 0
    head = (nx, ny)

print(cnt)