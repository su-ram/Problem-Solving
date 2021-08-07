limit = list(map(int, input().split()))

from collections import deque
que = deque([(0,0,limit[-1])])
weight = set()
isvisited = [[False] * (limit[1]+1) for _ in range(limit[0]+1)]
isvisited[0][0] = True
while que :
    node = que.popleft()
    if node[0] == 0 :
        weight.add(node[2])
    for i in range(3):
        for j in range(3):
            if i == j :continue
            # i -> j
            next = list(node)
            water = min(node[i], limit[j]-node[j])
            next[i] -= water
            next[j] += water
            if not isvisited[next[0]][next[1]]:
                isvisited[next[0]][next[1]] = True
                que.append(next)

[ print(i, end=' ') for i in sorted(list(weight))]