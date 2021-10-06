N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N) for _ in range(N)]

j = A[0][0]
while j < N:
    dp[0][j] += 1
    j += A[0][j]
i = A[0][0]
while i < N:
    dp[i][0] += 1
    i += A[i][0]

# for i in range(1, N):
#     for j in range(1, N):
#         for dx in range(i):
#             if A[dx][j] + dx == i:
#                 dp[i][j] += dp[dx][j]
#         for dy in range(j):
#             if A[i][dy] + dy == j:
#                 dp[i][j] += dp[i][dy]

for d in range(1, N):
    for i in range(1, N):
        for j in range(1, N):
            if A[i-d][j] ==d and dp[i-d][j]:
                dp[i][j] += dp[i-d][j]
            if A[i][j-d] == d and dp[i][j-d]:
                dp[i][j] += dp[i][j-d]

for row in dp:
    print(row)
print(dp[-1][-1])