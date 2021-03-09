from collections import deque

N, M = list(map(int, input().split()))

inputs = [0]*(N+1)
links = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    inputs[y] += 1
    links[x].append(y)

que = deque()

for i in range(1,N+1):
    if inputs[i] == 0:
        que.append(i)

orders = []
while que:

    node = que.popleft()
    orders.append(node)

    for n in links[node]:
        inputs[n] -= 1
        if inputs[n] == 0:
            que.append(n)

for node in orders:
    print(node, end=" ")
