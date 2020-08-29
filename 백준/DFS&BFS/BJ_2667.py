from collections import deque

def DFS(root):
    #재귀
    x, y = root

    nx = [0,0,-1,1]
    ny = [1,-1,0,0]

    for i in range(4):

        a, b = x + nx[i], y + ny[i]

        if 0 <= a < n and 0 <= b < n :
            if visited[a][b] == 0 and matrix[a][b] == 1:
                global  cnt
                cnt+=1
                visited[a][b] = 1
                DFS((a,b))








n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
result = []
for i in range(n):
    for k in range(n):
        if visited[i][k] == 0 and matrix[i][k] == 1 :
            visited[i][k]=1
            cnt = 1
            DFS((i,k))
            result.append(cnt)


print(len(result))
for i in sorted(result):
    print(i)

