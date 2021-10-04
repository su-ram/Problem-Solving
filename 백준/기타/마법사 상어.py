# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dirs = [0, (0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

def move(dir, clouds, cnt):

    dx, dy = dir
    new_clouds = []

    for cloud in clouds:
        nx, ny = cloud[0] + cnt * dx, cloud[1] + cnt * dy
        nx %= R
        ny %= R
        new_clouds.append((nx,ny))
        A[nx][ny] += 1


    dx = [-1,-1,1,1]
    dy = [1,-1,-1, 1]

    for cloud in new_clouds:
        c = 0
        for i in range(4):
            nx = cloud[0] + dx[i]
            ny = cloud[1] + dy[i]
            if 0 <= nx < R and 0 <= ny < R and A[nx][ny] > 0 :
                c += 1
        A[cloud[0]][cloud[1]] += c

    next_clouds = []
    for i in range(R):
        for j in range(R):
            if A[i][j] >= 2 and (i,j) not in new_clouds:
                A[i][j] -= 2
                next_clouds.append((i,j))

    return next_clouds


R, M = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(R)]

clouds = [(R-1,0), (R-2,0), (R-1,1), (R-2,1)]
for _ in range(M):
    d, c = map(int, input().split())
    clouds = move(dirs[d], clouds, c)



result = 0
for row in A:
    result += sum(row)
print(result)