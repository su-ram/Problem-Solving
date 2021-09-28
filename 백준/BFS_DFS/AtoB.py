A, B = map(int, input().split())
from collections import deque

def BFS(start):
    q = deque([(start, 0)])
    dist = B

    while q:
        now, d = q.popleft()

        if now < 1 : continue
        if now == A:
            dist = min(dist,d)
        if now % 2 == 0 :
            q.append((now//2, d+1))
        if now % 10 == 1 and now > 1:
            next = str(now)
            next = int(next[:-1])
            q.append((next, d+1))

    return dist + 1 if dist != B else -1
print(BFS(B))