n = int(input())
#그래프 표현 : 인접 행렬

matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

visited = [0]*(n+1)
parent_list= [0]*(n+1)
def DFS(root,parent):
    parent_list[root] = parent
    visited[root] = 1

    connected = []
    for i in range(1,n+1):
        if matrix[root][i] == 1:
            connected.append(i)
    for i in connected:
        if visited[i] == 0 :
            DFS(i, root)
    return 1


DFS(1,0)
for i in parent_list[2:]:
    print(i)



