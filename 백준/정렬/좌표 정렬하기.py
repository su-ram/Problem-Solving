n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
nums = sorted(arr, key=lambda x : (x[0], x[1]))
for n in nums:
    print(n[0], n[1])