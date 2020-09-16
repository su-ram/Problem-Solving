from collections import deque

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def connect(start):

    que = deque([start])
    cluster = []
    while que:

        node = que.popleft()

        if visited[node] == 1:continue

        visited[node] = 1
        cluster.append(node)

        for j in range(1,n+1):
            if graph[node][j] == 1 and visited[j] == 0 and j not in que:
                que.append(j)
    return cluster

cnt = 0

for i in range(1,n+1):
    if connect(i) != []:
        cnt+=1
print(cnt)






