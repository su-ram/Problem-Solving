n = int(input())
nums = list(range(n+1))
s, e = 1, 1
total = 0
ans = 0

while s <= n:

    if total < n:
        total += nums[e]
        e += 1
    elif total > n:
        total -= nums[s]
        s += 1
    elif total == n:
        total -= nums[s]
        ans += 1
        s += 1

print(ans)
