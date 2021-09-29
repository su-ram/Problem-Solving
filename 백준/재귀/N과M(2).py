N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def DFS(d,nums):
    global arr

    if d == M:
        print(' '.join(map(str,nums)))
        return nums

    for i in range(1, N+1):
        if arr[i-1] in nums: continue
        DFS(d+1, nums+[arr[i-1]])


DFS(0, [])
