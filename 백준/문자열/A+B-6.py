n = int(input())
nums = [tuple(map(int, input().split(','))) for _ in range(n)]

for num in nums:
    print(sum(num))