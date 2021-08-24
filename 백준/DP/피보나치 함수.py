t = int(input())
dp = [0] * (41)
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2, 41):
    dp[i] = list(map(lambda x : sum(x), zip(dp[i-1], dp[i-2])))
for i in range(t):
    index = int(input())
    print(' '.join(list(map(str, dp[index]))))

