l1, l2 = map(int,input().split())
from collections import deque
que = deque([(0,0)])
visited =[ [False] * (l2 + 1) for _ in range(l1 + 1)]
visited[0][0] = True
ans = set()

def add_que(node):
    if visited[node[0]][node[1]] == False:
        visited[node[0]][node[1]] = True
        que.append(node)

while que :
    now = que.popleft()

    ans.add(now[0])
    ans.add(now[1])

    add_que((l1,l2))
    add_que((l1, now[1]))
    add_que((now[0], l2))
    add_que((0, now[1]))
    add_que((now[0], 0))
    add_que((0,0))

    amount = min(l2-now[1], now[0])
    add_que((now[0]-amount, now[1]+amount))
    amount = min(l1-now[0], now[1])
    add_que((now[0] +amount, now[1]-amount))

ans.remove(0)
[ print(i, end=' ') for i in sorted(ans)]
