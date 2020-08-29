from collections import deque

# 입력값 받음
n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]

# 방문했는지 체크하기 위한 2차원 배열
visited = [[0] * m for _ in range(n)]
length = [[0]*m for _ in range(n)]
length[0][0] = 1
visited[0][0] = 1

# 상하좌우를 나타내기 위한 값들
nx = [0, 0, -1, 1]
ny = [1, -1, 0, 0]

queue = deque()
queue.append((0, 0))

while queue:

    x, y = queue.popleft()

    for i in range(4):

        a, b = x + nx[i], y + ny[i]

        if 0 <= a < n and 0 <= b < m:

            if visited[a][b] == 0 and matrix[a][b] == 1:

                visited[a][b] = 1
                length[a][b] = length[x][y] + 1
                queue.append((a, b))


print(length[n-1][m-1])