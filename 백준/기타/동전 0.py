N, K = map(int, input().split())
A = [ int(input()) for _ in range(N)]
cnt = 0
for a in A[::-1]:
    if K == 0: break
    if a <= K:
        x, y = divmod(K, a)
        cnt += x
        K = y
print(cnt)