from collections import deque

N = int(input())
inputs = [[0]*2] * (N+1)
links = [[] for _ in range(N+1)]
dp = [0] * (N+1)

for i in range(1, N+1):

    row = list(map(int, input().split()[:-1]))
    inputs[i] = [row[0], len(row[1:])]

    for node in row[1:]:
        links[node].append(i)

que = deque()

for i in range(N+1):

    dp[i] = inputs[i][0]
    if inputs[i][1] == 0:
        que.append(i)

while que:

    node = que.popleft()

    for n in links[node]:

        inputs[n][1] -= 1

        if inputs[n][1] == 0:
            que.append(n)

        dp[n] = max(dp[node]+inputs[n][0], dp[n])


for node in dp[1:]:
    print(node)