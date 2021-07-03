def get_candidates(index, arr):

    arr.append(nums[index])
    visited[index] = True

    if len(arr) == N:
        [print(_, end=" ") for _ in arr]
        print()
        return

    for i in range(N):
        if visited[i]:continue
        get_candidates(i, arr)
        del arr[-1]
        visited[i]=False

N = int(input())
nums = list(range(1, N+1))
for i in range(N):
    arr = []
    visited = [False for _ in range(N)]
    get_candidates(i,arr)
