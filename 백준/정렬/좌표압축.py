n = int(input())
nums = list(map(int, input().split()))
new_nums = sorted(set(nums))
counter = {}

for i in range(len(new_nums)):
    counter[new_nums[i]] = i

for n in nums:
    print(counter.get(n), end=' ')