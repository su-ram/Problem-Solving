n = int(input())

matrix = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt = 0
def DFS(x,y,color):
    stack = [(x,y)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while stack :

        node = stack.pop()
        x, y = node[0], node[1]
        visited[x][y] = 1

        for j in range(4):

            xx = x + dx[j]
            yy = y + dy[j]

            if 0 <= xx < n and 0 <= yy < n :
                if matrix[xx][yy] == color and visited[xx][yy] == 0 :
                    stack.append((xx,yy))

    return 1


for i in range(n):
    for j in range(n):
        if matrix[i][j] in ['R','G','B'] and visited[i][j] == 0 :
            cnt += DFS(i,j,matrix[i][j])

print(cnt, end=" ")

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        value = matrix[i][j]
        if value =='R':
            matrix[i][j] = 'G'


cnt = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] in ['G','B'] and visited[i][j] == 0 :
            cnt += DFS(i,j,matrix[i][j])

print(cnt)