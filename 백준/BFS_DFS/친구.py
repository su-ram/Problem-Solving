n = int(input())
adj = {}
for i in range(n):
    row = list(input())
    adj[i] = []
    for j in range(n):
        if row[j] == 'Y':
            adj[i].append(j)

ans = -1
for i in range(n):
    now = i
    cnt = len(adj.get(now))
    ff = []
    for j in adj.get(now):
        for friend in adj.get(j):
            if friend == now or friend in adj.get(now): continue
            if friend not in ff:
                cnt += 1
                ff.append(friend)
    ans = max(ans, cnt)
print(ans)