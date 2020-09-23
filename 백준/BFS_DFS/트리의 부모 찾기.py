n = int(input())
#그래프 표현 : 인접 리스트

matrix = [[] for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

visited = [0]*(n+1)
parent_list= [0]*(n+1)
def DFS(root,parent):

    visited[root] = parent
    for i in matrix[root]:
        if visited[i] == 0 :
            DFS(i,root)

DFS(1,-1)
for i in visited[2:]:
    print(i)



