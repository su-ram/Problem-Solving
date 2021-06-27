
from itertools import permutations

dwarfs = [int(input()) for _ in range(9)]

candidate = permutations(dwarfs, 7)

for c in candidate:
    if sum(c) == 100 :
        seven_dwarfs = sorted(list(c))
        [print(d) for d in seven_dwarfs ]
        break