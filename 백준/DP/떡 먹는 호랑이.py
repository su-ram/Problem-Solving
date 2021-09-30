D, K = map(int,input().split())
dp = [ [1]*(D+1) for _ in range(2)]
dp[0][2] = 0
if D > 3:
    for i in range(2):
        for j in range(4, D+1):
            dp[i][j] = dp[i][j-1] + dp[i][j-2]

a = dp[0][-1]
b = dp[1][-1]
A, B = False, False

for i in range(1, (K-b)//a+1):
    for j in range(1, (K-a)//b+1):
        if j < i: continue
        num = a*i + b*j
        if num == K:
            A = i
            B = j
            break
    if A is not False and B is not False:
        print(A)
        print(B)
        break