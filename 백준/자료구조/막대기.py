n = int(input())
arr = [ int(input()) for _ in range(n)]
now = arr[-1]
cnt = 1
for i in range(n-1, -1, -1):
    if arr[i] > now :
        now = arr[i]
        cnt += 1
print(cnt)