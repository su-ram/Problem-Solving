N, M = map(int, input().split())
town = []
chicken = []

for i in range(N):
    row = list(map(int, input().split()))
    town.append(row)
    start = 0

    if row.count(2):
        for j in range(N):
            if row[j] == 2:
                chicken.append((i,j))


from itertools import combinations
cases = combinations(chicken, M)

def get_chicken_dist(source, targets):
    dists = []
    for target in targets:
        dists.append(abs(source[0] - target[0]) + abs(source[1] - target[1]))
    return min(dists)

import math
min_dist = math.inf
for case in cases:
    dist = 0
    for i in range(N):
        for j in range(N):
            if town[i][j] == 1 :
                dist += get_chicken_dist((i,j), case)
    min_dist =min(dist, min_dist)

print(min_dist)



