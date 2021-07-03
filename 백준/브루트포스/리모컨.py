N = input()
M = int(input())
if M :
    disabled = set(map(int, input().split()))
else:
    disabled = []
able = set(range(10)).difference(disabled)

from itertools import product
cases = product(able, repeat=len(N))
cases2 = product(able, repeat=len(N)-1)
cases3 = product(able, repeat=len(N)+1)
import math

def get_min(cases):
    min_diff = math.inf
    for c in cases:
        if len(c) == 0 : continue
        num = int(''.join(map(str, c)))

        diff = len(str(num)) + abs(int(N) - num)
        min_diff = min(min_diff, diff)
    return min_diff

print(min(get_min(cases), get_min(cases2), get_min(cases3), abs(int(N) -100)))
