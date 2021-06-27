n = int(input())
from itertools import combinations

all = set(range(n))
power = [list(map(int, input().split())) for _ in range(n)]
candidate = combinations(range(n), n//2)
min_diff = 100

for c in candidate:
    star = c
    star_sum = 0
    power_pairs = combinations(c,2)
    for a, b in power_pairs:
        star_sum += power[a][b] + power[b][a]

    link = all - set(c)
    link_sum = 0
    power_pairs = combinations(link,2)
    for a, b in power_pairs:
        link_sum += power[a][b] + power[b][a]

    diff = abs(star_sum-link_sum)
    if diff < min_diff:
        min_diff = diff

print(min_diff)