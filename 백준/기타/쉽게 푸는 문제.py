N, M = map(int, input().split())
arr = []
num = 1
while len(arr) < M :
    if len(arr) + num >= M:
        length = M - len(arr)
        arr += [num] * length
    else:
        arr += [num] * num
    num += 1
print(sum(arr[N-1:M+1]))
