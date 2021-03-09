from collections import deque

M,N,H = map(int, input().split())

matrix = [[-1 for _ in range(N)] for _ in range(H)]
starts = []
dx, dy, dh = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

def Find_Starts(arr=[]):
#초기에 토마토들이 어디 있는지 찾는 함수

    starts = []

    for i in range(len(arr)):
        if arr[i] == 1:
            starts.append(i)

    return starts


#입력 받으면서 한줄씩 토마토가 이미 있는지 체크하여 starts 배열에 위치값을 넣어준다.
for i in range(H):
    for j in range(N):

        row = list(map(int, input().split()))
        matrix[i][j] = row

        for start in Find_Starts(row):
            starts.append((i,j,start))

def BFS(roots):
#처음 배열에 토마토가 있는 경우 1로 되어 있다 -> 날짜를 의미하기도 함.!!

    que = deque()
    que.extend(roots)

    while que:

        h, x, y  = que.popleft()

        for i in range(6):

            xx = x + dx[i]
            yy = y + dy[i]
            hh = h + dh[i]

            if 0 <= xx < N and 0 <= yy < M and 0 <= hh < H:

                if matrix[hh][xx][yy] == 0:
                    matrix[hh][xx][yy] = matrix[h][x][y] + 1
                    que.append((hh, xx, yy))

BFS(starts)

already = 0
days = -1

for i in matrix:
    for j in i:
        for k in j:
            if k == 0: #안 익은 토마토가 있는 경우
                already = -1

            days = max(k, days) # 가장 큰 값을 찾음 -> 가장 마지막 날 값을 구하기 위해.

if days == 1:
    print(0)
elif already == -1:
    print(-1)
else:
    print(days - 1)

