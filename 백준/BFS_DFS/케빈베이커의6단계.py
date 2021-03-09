from collections import deque

n, m = map(int, input().split())

#인접리스트로 표현
adj = [[] for _ in range(n+1)]

for i in range(m):

    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

board = [0] * (n+1)
def BFS(start):

    que = deque([(start,0)])
    visited = [False] * (n+1)

    while que:

        node, num = que.popleft()
        visited[node] = True
        board[node] += num
        if not visited[node]:

            for next in adj[node]:
                que.append((next, num+1))





for i in range(1,n+1):
    BFS(i)

print(board)