n, m = map(int, input().split())
arr = list(map(int,input().split()))
start, end = 0, 0
cnt = 0
while start < n :
    sub = arr[start:end]
    if sum(sub) == m :
        cnt += 1
        start += 1
    elif sum(sub) > m or end == n : start += 1
    elif sum(sub) < m and end < n : end += 1

print(cnt)