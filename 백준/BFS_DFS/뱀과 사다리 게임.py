N, M = map(int, input().split())
jumps = {}
for _ in range(N+M):
    s,t = map(int, input().split())
    jumps[s] = t

from collections import deque

def BFS(start,d):
    que = deque([(start,d)])
    visited = [False] * 101
    visited[start] = d

    while que:
        num, d = que.popleft()

        for i in range(1, 7):
            next = num + i
            if jumps.get(next):
                next = jumps.get(next)
            if 1 <= next <= 100 :
                if visited[next] is False:
                    que.append((next,d+1))
                    visited[next] = d + 1
                elif d + 1 < visited[next]:
                    visited[next] = d + 1
                    que.append((next, d + 1))

    print(visited[-1])


BFS(1,0)
