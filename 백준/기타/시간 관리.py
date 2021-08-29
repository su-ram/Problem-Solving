n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]
works.sort(key = lambda x : x[1])
gap = 0
start = works[0][1] - works[0][0]
for i in range(n):
    start += works[i][0]
    if start > works[i][1] :
        gap = max(gap, start - works[i][1])

start = works[0][1] - works[0][0] - gap
print(start if start >= 0 else -1)
