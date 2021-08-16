import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]
for _ in range(M+K):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1 :
        arr[cmd[1]-1] = cmd[2]
    if cmd[0] == 2 :
        print(sum(arr[cmd[1] - 1 : cmd[2]]))