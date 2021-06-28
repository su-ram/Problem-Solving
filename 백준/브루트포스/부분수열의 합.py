N, S = map(int, input().split())
arr = list(map(int, input().split()))


def DFS(i, sum):

    if i == N :
        return

    if sum + arr[i] == S :
        global cnt
        cnt += 1

    DFS(i+1, sum)
    DFS(i+1, sum+arr[i])

cnt = 0
DFS(0,0)
print(cnt)