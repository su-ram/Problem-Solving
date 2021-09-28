
def solve(start, arr, visited):
    now = start
    visited[start] = 1
    while True:
        next = arr[now]
        visited[next] = 1
        if next == start: break
        now = next


for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0]*(n+1)
    result = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            solve(i, arr,visited)
            result += 1
    print(result)



