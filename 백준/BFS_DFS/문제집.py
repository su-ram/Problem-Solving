N, M = map(int, input().split())
degree =[0] * (N+1)
graph =[[] for _ in range(N+1)]

for i in range(M):
    prev, post = map(int, input().split())
    degree[post] += 1
    graph[prev].append(post)

import heapq

heap = []
for i in range(1, N+1):
    if degree[i] == 0:
        heap.append(i)

heapq.heapify(heap)

while heap:

    node = heapq.heappop(heap)
    print(node, end=' ')
    for n in graph[node]:
        degree[n] -= 1
        if degree[n] == 0 :
            heapq.heappush(heap, n)



