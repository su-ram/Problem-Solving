
from collections import deque

def BFS(start):
    q = deque([start])
    visit = []
    while q:
        x,y,beer = q.popleft()
        if x == tx and y == ty :
            print('happy')
            return
        for s in store:
            dist = abs(x-s[0]) + abs(y-s[1])
            if 50 * beer >= dist and (s[0], s[1]) not in visit:
                q.append((s[0], s[1], beer))
                visit.append((s[0], s[1]))

    print('sad')
    return


for _ in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    store = []
    for _ in range(n):
        store.append(tuple(map(int, input().split())))
    tx, ty = map(int, input().split())
    store.append((tx,ty))
    BFS((sx,sy,20))
