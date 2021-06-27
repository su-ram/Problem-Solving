'''
주어진 수들 : nums 중에서 3가지의 수를 뽑는 모든 경우의 수를 구한다. -> 브루트포스
n * (n-1) * (n-2)
반복문을 순회하면서 limit값을 넘지 않으면서 가장 큰 합을 계속 갱신해 나간다.
'''

num, limit = map(int, input().split())
nums = list(map(int, input().split()))
from itertools import permutations

candidate = permutations(nums,3)
max_sum = -1

for p in candidate:

    sum_tmp = sum(p)

    if sum_tmp > max_sum and sum_tmp <= limit:
        max_sum = sum_tmp

print(max_sum)