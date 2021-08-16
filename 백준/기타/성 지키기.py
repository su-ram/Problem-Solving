n, m =map(int, input().split())
row = [0] * n
col = [0] * m

for i in range(n):
    arr = list(input())
    for j in range(m):
        if arr[j] == 'X':
            row[i] = 1
            col[j] = 1

print(max(row.count(0), col.count(0)))
