N, k = map(int, input().split())
out =[]
from collections import deque
que = deque([i+1 for i in range(N)])

while len(out) < N:
    for _ in range(k-1):
        que.append(que.popleft())
    out.append(que.popleft())

print('<', end='')
print(', '.join(list(map(str, out))), end='')
print('>')