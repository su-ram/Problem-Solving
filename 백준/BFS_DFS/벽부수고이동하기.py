from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[[-1]*2 for _ in range(M)]for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0,0)]
visited[0][0][0] = 1

while queue:
    x, y, cnt = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny][cnt] == -1 and matrix[nx][ny] == '0':
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                queue.append((nx,ny,cnt))

            if matrix[nx][ny] == '1' and cnt == 0 and visited[nx][ny][1]==-1:
                visited[nx][ny][1] = visited[x][y][cnt] + 1
                queue.append((nx,ny,1))

answer1, answer2 = visited[N-1][M-1]

if answer1 == -1 and answer2 != -1:
    print(answer2)
elif answer2 == -1 and answer1 != -1:
    print(answer1)
else:
    print(min(answer2,answer1))