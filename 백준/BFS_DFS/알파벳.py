import sys

sys.stdin = open('input.txt', 'r')
r, c = map(int, input().split())
matrix = []
pool = [0]*27
maxcnt = 1

curcnt = 1

for i in range(r):
    temp = []
    for j in input().rstrip():
        temp.append(ord(j)-65)
    matrix.append(temp)


dx = [0,0,-1,1]
dy = [1,-1,0,0]


def DFS(x,y):
    print("I visit ", x, y)
    value = matrix[x][y]
    pool[value] = 1

    for i in range(4):

        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < r and 0 <= yy < c:

            newnode = matrix[xx][yy]
            if pool[newnode] == 1 : continue
            global curcnt
            global maxcnt
            curcnt+=1
            maxcnt = max(maxcnt, curcnt)
            DFS(xx,yy)

    curcnt -= 1
    pool[value] = 0

DFS(0,0)
print(maxcnt)