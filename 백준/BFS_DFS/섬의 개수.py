import sys
from collections import deque

sys.stdin = open('input.txt.txt', 'r')


def BFS(start):

    q = deque()
    q.append(start)
    
    dx = [0,0,-1,1,-1,-1,1,1]
    dy = [1,-1,0,0,-1,1,-1,1]

    while q : 
        #print(q)
        node = q.popleft()
        x , y = node[0], node[1]
        visited[x][y] = 1

        for k in range(8):

            x2 = x + dx[k]
            y2 = y + dy[k]

            if 0 <= x2 < height and 0 <= y2 < width:
                if matrix[x2][y2] == 1 and visited[x2][y2] == 0 and (x2,y2) not in q:
                    q.append((x2,y2))


    return 1

while (True):

    width, height = map(int, input().split())
    visited = [[0]*width for _ in range(height)]

    if width == 0 and height == 0 : break

    matrix = []

    for _ in range(height):
        matrix.append(list(map(int, input().split())))
   
    island = 0 
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 1 and visited[i][j] == 0 :
                island += BFS((i,j))
    print(island)




