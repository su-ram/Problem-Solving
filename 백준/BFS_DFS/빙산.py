row, col = map(int,input().split())
iceberg = [ list(map(int, input().split())) for _ in range(row)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def oneYear(ice):

    melted = []
    gone = []

    for node in ice:
        x, y = node[0], node[1]

        for _ in range(4):
            xx, yy = x + dx[_], y + dy[_]
            if iceberg[xx][yy] == 0:
                melted.append((x,y))
    for node in melted:
        x, y = node[0], node[1]
        if iceberg[x][y] > 0 :
            iceberg[x][y] -= 1
            if iceberg[x][y] == 0:
                gone.append((x, y))


    return gone

def check():

    for i in range(row):
        for j in range(col):
            if iceberg[i][j] > 0 :
                return True

    return False

def DFS(start):
    stack = [start]
    while stack:

        node = stack.pop()
        x , y = node[0], node[1]
        visited[x][y] = 1

        for i in range(4):

            xx, yy = x + dx[i], y + dy[i]

            if 0 <= xx < row and 0 <= yy <col and iceberg[xx][yy] > 0 and visited[xx][yy] == 0:
                stack.append((xx,yy))

    return 1

ice = []
for i in range(row):
    for j in range(col):
        if iceberg[i][j] > 0 :
            ice.append((i,j))

year = 0
while check():
    #빙산이 다 녹지 않을 때까지 반복

    new_melted = oneYear(ice)
    year +=1

    if new_melted != []:
        for i in new_melted:
            ice.remove(i)

    visited = [[0] * col for _ in range(row)]
    group = 0
    for i in range(row):
        for j in range(col):
            if iceberg[i][j] > 0 and visited[i][j] == 0:

                group += DFS((i,j))
    if group >= 2:
        break
if group == 0 : year = 0
print(year)