import sys
#DFS 백트래킹을 이용하는 문제. 공부 더 필요......ㅠ

r, c = map(int, input().split())
matrix = []
pool = [0]*26

cnt = 0
maxcnt = 0
for i in range(r):
    temp = []
    for j in input().rstrip():
        temp.append(ord(j)-65)
    matrix.append(temp)


dx = [0,0,-1,1]
dy = [1,-1,0,0]

arr=[]
def promising(x,y):
    if pool[matrix[x][y]] == 1 : return False
    else: return True

def DFS(x,y):
    #
    arr.append((x,y))
    print(arr)
    global cnt
    global maxcnt
    cnt += 1
    maxcnt = max(cnt, maxcnt)

    value = matrix[x][y]
    pool[value] = 1

    candidate = []

    for i in range(4):

        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < r and 0 <= yy < c and promising(xx,yy):
            candidate.append((xx,yy))

    if candidate == [] :
        temp = arr.pop()
        cnt -= 1
        i = temp[0]
        j = temp[1]
        pool[matrix[i][j]] = 0
        return
    else:
        for i in candidate:
            DFS(i[0], i[1])
    temp = arr.pop()
    cnt -= 1
    i = temp[0]
    j = temp[1]
    pool[matrix[i][j]] = 0

DFS(0,0)

print(cnt,maxcnt)


