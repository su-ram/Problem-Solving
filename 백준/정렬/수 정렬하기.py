N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(1, N):
    current = i

    for j in range(i-1, -1, -1):
        if nums[current] < nums[j]:
            tmp = nums[current]
            nums[current] =nums[j]
            nums[j] = tmp
            current = j

[print(n) for n in nums]


