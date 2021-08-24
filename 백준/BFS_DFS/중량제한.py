n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b,w))
    adj[b].append((a,w))
from collections import deque

source, target = map(int, input().split())
def BFS(weight):
    que = deque([source])
    visited = [False] * (n+1)
    visited[source] = True
    while que:
        node = que.popleft()
        for next in adj[node]:
            if visited[next[0]] is False and next[1] >= weight:
                que.append(next[0])
                visited[next[0]] = True
    return True if visited[target] else False

start = 1
end = 1000000000
result = start
while start <= end :
    mid = (start+end) // 2
    if BFS(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)


