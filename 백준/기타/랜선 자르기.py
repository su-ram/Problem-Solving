K, N = map(int, input().split())
nums = [ int(input()) for _ in range(K)]
start = 1
end = max(nums)+1
result = 0

while start <= end:
    mid = (start+end) // 2
    if mid == 0:break
    total = 0
    for n in nums:
        total += n // mid

    if total >= N :
        if mid > result:
            result = mid
        start = mid + 1

    if total < N :
        end = mid - 1

print(result)
