a = input()
b = input()
lena = len(a)
lenb = len(b)
dp = [ [0]*(lenb + 1) for _ in range(lena+1)]

for i in range(1, lena+1):
    for j in range(1, lenb+1):
        if a[i-1] == b[j-1]:
            dp[i][j]  = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for row in dp:
    print(row)