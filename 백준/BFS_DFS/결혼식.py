N = int(input())
adj = [[] for _ in range(N+1)]
import math

for _ in range(int(input())):
    i,j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

visited = [False] * (N+1)
friend = [math.inf]*(N+1)
friend[1] = 0

for i in range(1, N+1):
    if friend[i] == math.inf:continue
    if friend[i] < 2:
        next = friend[i] + 1
    else:
        next = math.inf
    for j in adj[i]:
        if visited[j] is True: continue
        friend[j] = min(friend[j], next)
    visited[i] = True
result = 0
for f in friend[1:]:
    if f in [1,2]:
        result += 1
print(result)