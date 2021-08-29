n, m = map(int, input().split())
matrixa = [ list(map(int, list(input()))) for _ in range(n)]
matrixb = [ list(map(int, list(input()))) for _ in range(n)]

def switch(start):
    x,y = start
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrixa[i][j] = 1-matrixa[i][j]


cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if matrixa[i][j] != matrixb[i][j] :
            switch((i,j))
            cnt += 1


for i in range(n):
    for j in range(m):
        if matrixa[i][j] != matrixb[i][j]:
            print(-1)
            exit(0)

print(cnt)

