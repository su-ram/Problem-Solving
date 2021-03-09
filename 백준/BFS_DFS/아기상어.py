from heapq import heappop, heappush

N = int(input())
matrix = []
current_size = 2
dx, dy = [0,0,-1,1], [-1,1,0,0]
visited = [[False] * N for _ in range(N)]
que = []
seconds = 0
cnt = 0

for i in range(N):

    matrix.append(list(map(int, input().split())))

    for j in range(N):
        if matrix[i][j] == 9 :
            heappush(que,(0,i,j))
            matrix[i][j] = 0

while que:

    distance, i, j = heappop(que)

    if 0 < matrix[i][j] < current_size:

        cnt += 1
        seconds += distance
        matrix[i][j] = 0
        if cnt == current_size:
            current_size += 1
            cnt = 0
        visited = [[False] * N for _ in range(N)]
        distance = 0
        que = []

    for index in range(4):
        xx = i + dx[index]
        yy = j + dy[index]
        dd = distance + 1

        if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy] and matrix[xx][yy] <= current_size:

            visited[xx][yy] = True
            heappush(que,(dd, xx, yy))

print(seconds)

