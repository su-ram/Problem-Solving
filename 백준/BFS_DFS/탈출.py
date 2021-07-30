from collections import deque
import math


n, m = map(int, input().split())
ponds =[]
graph = [[math.inf]*m for _ in range(n)]

for i in range(n):
    row = list(input())

    for j in range(m):
        if row[j] == 'D':
            dest = (i,j)
            graph[i][j] = -1
        if row[j] == 'S':
            source = (i,j)
        if row[j] == '*':
            ponds.append((i,j))
        if row[j] == 'X':
            graph[i][j] = -1



def BFSWater(graph, start):

    que = deque([start])
    visited[start[0]][start[1]] = True

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while que:
        node = que.popleft()

        for i in range(4):
            xx = node[0] +dx[i]
            yy = node[1] +dy[i]

            if 0 <= xx < n and 0 <= yy < m:
                if not visited[xx][yy] and graph[xx][yy] != -1:
                    que.append((xx,yy))
                    visited[xx][yy] = True
                    graph[xx][yy] = min(graph[node[0]][node[1]]+1, graph[xx][yy])

def escape(graph, start):

    que = deque([start])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False]*m for _ in range(n)]

    visited[start[0]][start[1]] = True

    while que:
        node = que.popleft()

        for i in range(4):
            xx = node[0] +dx[i]
            yy = node[1] +dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if not visited[xx][yy] and graph[xx][yy] and route[node[0]][node[1]] +1 < graph[xx][yy]:
                    que.append((xx,yy))
                    visited[xx][yy] = True
                    route[xx][yy] = route[node[0]][node[1]] + 1


for i in ponds:
    visited = [[False] * m for _ in range(n)]
    graph[i[0]][i[1]] = 0
    BFSWater(graph, i)


route = [[0]*m for _ in range(n)]
graph[dest[0]][dest[1]] = math.inf
escape(graph, source)
print(route[dest[0]][dest[1]] if route[dest[0]][dest[1]] else 'KAKTUS')
