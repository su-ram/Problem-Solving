#백준 7576 토마토
#BFS

#입력
m,n = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]

#익어 있는 토마토 위치 찾기 값이 1인 것
roots = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1: roots.append((i,j))

def BFS_Search(roots):
#roots에 저장되어 있는 노드의 상하좌우를 익은 토마토로 바꾸는 함수


    stack = roots
    nx = [0,0,-1,1]
    ny = [1,-1,0,0]
    new_roots = []

    while stack :

        node = stack.pop()

        for i in range(4):

            a, b = node[0] + nx[i], node[1] + ny[i]

            if 0 <= a < n and 0 <= b < m :
                if visited[a][b] == 0 and tomato[a][b] == 0 :
                    visited[a][b] = 1
                    tomato[a][b] = 1
                    new_roots.append((a,b))

    return new_roots
def check():
    #토마토들이 모두 익었는지 확인하는 함수
    for _ in tomato:
        if 0 in _ :
            return False

    return True


days = 0
visited = [ [0]*m for _ in range(n)]

for _ in range(n*m):

    if not check():
        roots = BFS_Search(roots)
    else:
        break
    days += 1

if days == m*n : days = -1
print(days)

