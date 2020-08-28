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

