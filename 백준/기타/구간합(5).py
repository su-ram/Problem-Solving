N, M = map(int,input().split())
a=[[0]*(N+1)]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    a.append(row)

num = 0
for j in range(N):
    num += a[0][j]
    a[0][j] = num

num = 0
for i in range(N):
    num += a[i][0]
    a[i][0] = num

for i in range(1, N+1):
    for j in range(1, N+1):
        a[i][j] = a[i-1][j] + a[i][j-1] - a[i-1][j-1] + a[i][j]


for _ in range(M):
    sx, sy, tx, ty = map(int, input().split())
    area1 = (tx, sy-1)
    area2 = (sx-1, ty)
    area3 = (min(area1[0], area2[0]), min(area1[1], area2[1]))
    print(a[tx][ty] - a[area1[0]][area1[1]] - a[area2[0]][area2[1]] + a[area3[0]][area3[1]])


