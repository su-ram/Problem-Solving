N = int(input())
candy = [ list(input()) for _ in range(N)]
from collections import deque

def eat_candy(start, N, candy, dirs):


    q = deque([start])
    visited = set([start])
    cnt = 0
    color = candy[start[0]][start[1]]
    while q:
        x, y = q.popleft()
        cnt += 1
        for d in dirs:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and candy[nx][ny] == color:
                q.append((nx,ny))
                visited.add((nx,ny))
    return cnt


def search(N, candy, dirs):
    cnt = -1
    for i in range(N):
        for j in range(N):
            cnt = max(cnt, eat_candy((i,j), N, candy, dirs[:2]))
            #print(eat_candy((i,j), N, candy, dirs[:2]))
            cnt = max(cnt, eat_candy((i,j), N, candy, dirs[2:]))
            #print(eat_candy((i, j), N, candy, dirs[2:]))
    return cnt


def solution(N, candy):

    dirs = [(0,-1), (0,1), (1,0), (-1,0)]
    answer = search(N, candy, dirs)

    for i in range(N):
        for j in range(N):
            for d in dirs:
                nx, ny = i + d[0], j + d[1]
                if 0 <=nx <N and 0 <= ny < N and candy[i][j] != candy[nx][ny]:
                    candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]
                    answer = max(answer,eat_candy((i,j), N, candy, dirs[:2]))
                    answer = max(answer, eat_candy((i, j), N, candy, dirs[2:]))
                    answer = max(answer, eat_candy((nx, ny), N, candy, dirs[:2]))
                    answer = max(answer, eat_candy((nx, ny), N, candy, dirs[2:]))
                    candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]
                    if answer == N:
                        return answer

    return answer


print(solution(N, candy))


