#백준 1697 숨바꼭질

from collections import deque

#입력
n, k = map(int, input().split())
q = deque()
visited={}
visited[n] = 0
cnt = 0
q.append(n)
add = [0, 1, -1]
while q :
    node = q.popleft()
    add[0] = node
    cnt += 1
    for i in range(3):
        val = node + add[i]
        visited[val] = cnt
        q.append(val)