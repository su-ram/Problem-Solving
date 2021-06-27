L, C = map(int, input().split())
characters = list(input().split())
vowels = set(['a', 'e', 'i', 'o', 'u'])
from itertools import permutations

characters = sorted(characters)
candidates = permutations(characters,L)
for c in candidates:

    vowwl_check = vowels.intersection(c)

    if len(vowwl_check) < 1 or len(vowwl_check) > L-2:
        continue

    isordered = True
    for i in zip(c, c[1:]):
        if ord(i[1]) - ord(i[0]) < 0 :
            isordered = False
            break

    if not isordered:
        continue

    print(''.join(c))

