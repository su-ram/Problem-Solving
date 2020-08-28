#백준 1697 숨바꼭질

from collections import deque

#입력
n, k = map(int, input().split())

shortest = {}

queue = deque()
queue.append(n)

cnt = 0
root = []

while queue:


    node = queue.popleft()
    root.append(node)

    if node == k : break

    queue.extend([node*2, node-1, node+1])
    cnt += 1
    shortest[node*2] = cnt
    shortest[node-1] = cnt
    shortest[node+1] = cnt
    print(shortest)


