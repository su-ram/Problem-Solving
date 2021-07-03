N = int(input())
nums = list(map(int,input().split()))

from itertools import permutations
candidates =permutations(nums)
import math
max_total = -math.inf

# for candidate in candidates:
#     print(candidate)
#     total = sum(list(map(lambda x :  abs(x[0]-x[1]), zip(candidate[:-1], candidate[1:]))))
#     max_total = max(max_total, total)
#
# print(max_total)

#백트래킹으로 풀기
def get_candidates(index, arr):

    arr.append(nums[index])
    visited[index] = True

    if len(arr) == N:
        total = sum(list(map(lambda x: abs(x[0] - x[1]), zip(arr[:-1], arr[1:]))))
        global max_total
        max_total = max(max_total, total)
        print(arr)
        return

    for i in range(N):
        if visited[i]:continue
        get_candidates(i, arr)
        del arr[-1]
        visited[i]=False

N = 3
nums = [1,2,3]
for i in range(N):
    arr = []
    visited = [False for _ in range(N)]
    get_candidates(i,arr)

print(max_total)