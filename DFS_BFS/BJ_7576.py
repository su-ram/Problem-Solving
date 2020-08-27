from collections import deque
print("I'm changed!")
m,n = map(int,input().split())
tmt = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def BFS(roots):

    nx , ny = [0,0,-1,1], [1,-1,0,0]

    queue = deque()
    queue.extend(roots)

    next=[]



    while queue:


        node = queue.popleft()


        for k in range(4):

            a, b = node[0] + nx[k], node[1] + ny[k]


            if 0 <= a < n and 0 <= b < m :

                if visited[a][b] == 0 and tmt[a][b] == 0 :
                    tmt[a][b] = 1
                    visited[a][b] = 1
                    next.append((a,b))


    return next

def check():
    for _ in tmt:
        if 0 in _:
            return False
    return True

roots=[]

for i in range(n):
    for j in range(m):

        if tmt[i][j] == 1:
            roots.append([(i,j)])

cnt=0
for i in range(n*m):
    if check():
        break
    for k in range(len(roots)):
        newroot=BFS(roots[k])
        roots[k] = newroot
    cnt+=1
if cnt == n*m:
    print(-1)
else:
    print(cnt)




