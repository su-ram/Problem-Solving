from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
#세로, 가로

lab = [list(map(int, input().split())) for _ in range(n)]

virus = []
space = []

def spread(start, matrix):


    visited=[[0]*m for _ in range(n)]
    q = deque()
    q.extend(list(start))

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:

        node = q.popleft()

        x, y = node[0], node[1]
        visited[x][y] = 1
        matrix[x][y] = 2

        for _ in range(4):

            x2 = x + dx[_]
            y2 = y + dy[_]

            if 0 <= x2 < n and 0 <= y2 < m:
                if matrix[x2][y2] == 0 and visited[x2][y2] == 0 :
                    q.append((x2,y2))


    return matrix
def check(matrix):

    hap = 0

    for i in matrix:
        hap += i.count(0)

    return hap



for i in range(n):

    for j in range(m):

        if lab[i][j] == 2 :
            virus.append((i,j))
        if lab[i][j] == 0 :
            space.append((i,j))

candidate = combinations(space,3)
maxvalue = set()
for i in candidate:

    temp = copy.deepcopy(lab)

    # 벽 세움
    for node in i :
        x, y = node[0], node[1]
        temp[x][y] = 1

    result = spread(virus,temp)
    maxvalue.add(check(result))
print(max(maxvalue))







