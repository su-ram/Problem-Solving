
def solve(sticker, length):

    dp = [ [0] * (length+1) for _ in range(2)]
    dp[0][1] = sticker[0][0]
    dp[1][1] = sticker[1][0]

    for j in range(2, length+1):
        prev = max(dp[0][j-2], dp[1][j-2])
        dp[0][j] = max(prev+sticker[0][j-1], dp[1][j-1]+sticker[0][j-1])
        dp[1][j] = max(prev+sticker[1][j-1], dp[0][j-1]+sticker[1][j-1])

    print(max(dp[0][-1], dp[1][-1]))


for _ in range(int(input())):
    sticker = []
    length = int(input())
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))
    solve(sticker, length)