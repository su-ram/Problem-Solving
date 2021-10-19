n, m = map(int, input().split())


from collections import deque


def solution(n, m):
    q = deque([(n, 0)])
    d = [-1, 1]
    visited = [False] * (100001)
    visited[n] = 0
    
    while q :
        x, dist = q.popleft()

        for dx in d:
            nx = x + dx
            if 0 <= nx <= 100000:
                if visited[nx] is False or dist + 1 < visited[nx]:
                    q.append((nx,dist+1))
                    visited[nx] = dist + 1

        nx = x * 2
        if 0 <= nx <= 100000:
            if visited[nx] is False or dist < visited[nx]:
                q.append((nx, dist))
                visited[nx] = dist


    return visited[m]


print(solution(n,m))