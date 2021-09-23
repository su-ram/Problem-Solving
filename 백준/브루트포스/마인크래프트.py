import math

N, M, B = map(int, input().split())
land = {}
result = (math.inf, -math.inf)


for _ in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        cnt = land.get(row[j], 0)
        land[row[j]] = cnt + 1


def solve(h):
    cnt = [0,0]
    seconds = 0
    for k, v in land.items():
        if k > h :
            cnt[0] += (k-h) * v
            seconds += (k-h)*2*v
        elif k < h :
            cnt[1] += abs(k-h) * v
            seconds += abs(k-h)*v
    return cnt, seconds


for i in range(max(land.keys())+1):
    cnt, seconds = solve(i)
    if B + cnt[0] < cnt[1]: continue
    print(cnt, seconds, i)
    if seconds <= result[0] and i > result[1]:
        result = (seconds, i)
print(result[0], result[1])