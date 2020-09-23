import sys


sys.stdin = open('input.txt.txt', 'r')

m, n, k = map(int, input().split())

matrix = [[0]*(n) for _ in range(m)]

# m 세로 n 가로

def square(points):


    left_down = (points[0],points[1])
    right_top = (points[2],points[3])

    width, height = right_top[0] - left_down[0], right_top[1]-left_down[1]
    offset_x = m - (left_down[1]+height)
    offset_y = left_down[0]
    for x in range(height):
        for y in range(width):
            matrix[offset_x+x][offset_y+y] = 1


    return 0



for i in range(k):
    points = list(map(int, input().split()))
    square(points)

visited = [[0]*n for _ in range(m)]


def BFS(start):

    stack = []
    stack.append(start)

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    area = 0

    while stack :

        node = stack.pop()
        x, y = node[0], node[1]
        visited[x][y] = 1
        area += 1

        for k in range(4):
            x2 = x + dx[k]
            y2 = y + dy[k]

            if 0 <= x2 < m and 0 <= y2 < n :
                if matrix[x2][y2] == 0 and visited[x2][y2] == 0 and (x2,y2) not in stack :
                    stack.append((x2, y2))

    return area

result = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0 and visited[i][j] == 0 :
            result.append(BFS((i,j)))

print(len(result))
for i in sorted(result):
    print(i, end=" ")
    