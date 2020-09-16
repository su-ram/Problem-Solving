from collections import deque

T = int(input())

def worm(start):

    q = deque([start])

    while q:
        print(q)
        node = q.popleft()
        x,y=node[0],node[1]

        visited[x][y] = 1

        dx=[0,0,-1,1]
        dy=[1,-1,0,0]

        for k in range(4):

            new_x=x+dx[k]
            new_y=y+dy[k]

            if 0 <= new_x < n and 0 <= new_y < m:
                if cabb[new_x][new_y] == 1 and visited[new_x][new_y] == 0 and (new_x,new_y) not in q:
                    q.append((new_x,new_y))


    return 1


for _ in range(T):

    m,n,k=map(int,input().split())
    #가로, 세로, 배추 위치 개수
    cnt = 0
    cabb = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]


    for _ in range(k):
        x,y = map(int, input().split())
        cabb[y][x] = 1

    for i in range(n):
        for j in range(m):
            if cabb[i][j] == 1 and visited[i][j] == 0:
                cnt += worm((i,j))

    print(cnt)
