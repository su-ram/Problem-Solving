L, C = map(int, input().split())
characters = list(input().split())
vowels = set(['a', 'e', 'i', 'o', 'u'])
from itertools import combinations

characters.sort()
candidates = combinations(characters,L)

for c in candidates:

    vowwl_check = vowels.intersection(c)

    if len(vowwl_check) < 1 or len(vowwl_check) > L-2:
        continue

    isordered = True
    for i in range(L-1):
        if c[i+1] < c[i] :
            isordered = False
            break

    if not isordered:
        continue

    print(''.join(c))

