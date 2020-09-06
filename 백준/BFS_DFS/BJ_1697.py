from collections import deque

n, k = map(int, input().split())

def bfs(n):
    queue = deque()
    queue.append((n, 0))
    visited = [False] * 100010

    while queue:
        cur_node, cur_time = queue.popleft()
        for nxt in [cur_node + 1, cur_node - 1, cur_node * 2]:
            if nxt < 0 or nxt > 100000:
                continue
            if nxt == k:
                return cur_time + 1
            elif not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, cur_time + 1))

if n == k:
    print(0)
else:
    print(bfs(n))
