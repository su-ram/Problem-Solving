

for _ in range(int(input())):
    n = int(input())
    dp= [0] *(n+1)
    arr = list(map(int, input().split()))
    print(sum(arr))
    for i in range(2, n+1):
        dp[i] = sum(arr[:i]) + dp[i-1]
    print(dp)
    for i in range(3,n+1):
        dp[i]= min(dp[i-1]+sum(arr[:i]), dp[i-2]+arr[i-1]+arr[i-2]+sum(arr[:i]))




    print(dp)
