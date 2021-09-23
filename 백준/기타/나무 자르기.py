N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
height = -1

while start <= end:
    mid = (start+end) // 2
    total = 0
    for tree in trees:
        if tree > mid :
            total += tree - mid

    if total >= M :
        start = mid + 1

    if total < M :
        end = mid - 1
print(end)